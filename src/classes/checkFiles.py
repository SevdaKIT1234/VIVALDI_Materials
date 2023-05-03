"""checkFiles.py.

Main script for converting KIT research and measurements into the OpenMaterial conform format.
This code is part of the VIVALDI public funded project.

Check if the generated files are valid and follwong the OpenMaterial standard.
"""

import json as j
import os

from jsonschema import validate

__author__ = "Sandro Reith"
__project__ = "VIVALDI"
__copyright__ = "Copyright 2022, Continental AG"
__credits__ = ["Sandro Reith", "Sevda Abadpour"]
__version__ = "1.0.0"
__maintainer__ = "Sandro Reith"
__email__ = "sandro.reith@continental.com"
__status__ = "Production"


class CheckValidJson:
    """check if the generated json files following the schema of the OpenMaterial design."""

    def __init__(self):
        """Init class."""
        print("init")
        self.absolute_path = os.path.dirname(__file__)
        relative_path = "..\\template"
        self.schemaDir = os.path.join(self.absolute_path, relative_path)
        self.schema_asset_info = {}
        self.schema_material_params = {}
        self.schema_permeability = {}
        self.schema_permittivity = {}

    def getSchema(self, file):
        """Load the given schema available."""
        with open(file, "r", encoding="utf8") as file:
            schema = j.load(file)
        return schema

    def loadTemplates(self):
        """Load the schames from template folder."""
        if os.path.isdir(self.schemaDir):
            filenames = next(os.walk(self.schemaDir), (None, None, []))[2]  # [] if no file
            for file in filenames:
                if file.__contains__("OpenMaterial_asset_info.schema.json"):
                    self.schema_asset_info = self.getSchema(os.path.join(self.schemaDir, file))
                if file.__contains__("OpenMaterial_material_parameters.schema.json"):
                    self.schema_material_params = self.getSchema(os.path.join(self.schemaDir, file))
                elif file.__contains__("OpenMaterial_permeability_data.schema.json"):
                    self.schema_permeability = self.getSchema(os.path.join(self.schemaDir, file))
                elif file.__contains__("OpenMaterial_permittivity_data.schema.json"):
                    self.schema_permittivity = self.getSchema(os.path.join(self.schemaDir, file))
                else:
                    print("Not used: ", file)
        else:
            print("EROOR::schema folder is not available ", self.schemaDir)

    def validateJsonViaSchema(self, schema, jsonData):
        """Check if json following the defined schema.

        Args:
            schema (_type_): target schema
            jsonData (_type_): json file for validation

        Returns:
            _type_: true if validated, otherwise false
        """
        try:
            validate(instance=jsonData, schema=schema)
        except schema.exceptions.ValidationError as err:
            print(err)
            return False
        return True


if __name__ == "__main__":
    val = CheckValidJson()
    val.loadTemplates()
