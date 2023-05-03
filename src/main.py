"""main.py.

Main script for converting KIT research and measurements into the OpenMaterial conform format.
This code is part of the VIVALDI public funded project.
"""

import copy
import json
import os
from datetime import datetime

from classes.checkFiles import CheckValidJson as ValidateJson
from classes.readerTemplate import open_material_template as Template
from classes.readRawData import raw_data_reader as RawData

__author__ = "Sandro Reith"
__project__ = "VIVALDI"
__copyright__ = "Copyright 2022, Continental AG"
__credits__ = ["Sandro Reith", "Sevda Abadpour"]
__version__ = "1.0.0"
__maintainer__ = "Sandro Reith"
__email__ = "sandro.reith@continental.com"
__status__ = "Production"

lightspeed = 2.998e8


class open_material_data_set(Template, RawData):
    """Writting the OpenMaterial Output."""

    def __init__(material):
        """Init main class for VIALDI OpenMaterial.

        Args:
            material (_type_): self
        """
        super()

        material.absolute_path = os.path.dirname(__file__)
        relativePathMaterials = "..\\materials"
        material.materialsDir = os.path.join(material.absolute_path, relativePathMaterials)
        material.startTime = datetime.now().strftime("%Y.%m.%d %H:%M:%S")

        material.material_params = {}
        material.permeability = {}
        material.permittivity = {}
        material.Template = Template()
        material.rawData = RawData()
        material.schema = ValidateJson()

        material.init_struct_from_template()

    def get_material_names(self):
        """Get List of material names.

        Returns:
            _type_: list
        """
        return self.rawData.MaterialName

    def fill_json(self, name):
        """Call all filler functions.

        Args:
            name (_type_): material name
        """
        self.fill_material_json(name)
        self.fill_permittivity_json(name)

    def init_struct_from_template(self):
        """Generate OpenMaterial Struct from Class."""
        self.set_material_json(self.Template.material_params)
        self.set_permittivity_json(self.Template.permittivity)
        self.set_permeability_json(self.Template.permeability)

    def return_copyright(self):
        """Return fixed CopyRight.

        Returns:
            _type_: copyrigh info
        """
        return "(C) 2023, Karlsruhe Institute of Technology"

    def return_generator(self):
        """Return fix gnerator.

        Returns:
            _type_: generator
        """
        return "VIVALDI OpenMaterial Python Script"

    def return_creator(self):
        """Return fixed creator.

        Returns:
            _type_: creator
        """
        return "Karlsruhe Institute of Technology and Continental AG"

    def return_time(self):
        """Return programm start time as file genration time."""
        self.startTime

    def return_uuid(self, name):
        """ID uuid for material.

        Args:
            name (_type_): material name

        Returns:
            _type_: uuid
        """
        return self.rawData.uuid.loc[self.rawData.uuid["material"] == name]

    def fill_material_json(self, name):
        """Add loaded raw data to material json."""
        j_temp = copy.deepcopy(self.material_params)
        uuid = self.return_uuid(name)

        # assets
        j_temp["asset"]["copyright"] = self.return_copyright()
        j_temp["asset"]["generator"] = self.return_generator()
        j_temp["asset"]["version"] = __version__
        j_temp["asset"]["extensions"]["OpenMaterial_asset_info"]
        j_temp["asset"]["extensions"]["OpenMaterial_asset_info"]["asset_type"] = "material"
        j_temp["asset"]["extensions"]["OpenMaterial_asset_info"]["id"] = uuid["uuid"].item()
        j_temp["asset"]["extensions"]["OpenMaterial_asset_info"]["title"] = "_".join(["material", name])
        j_temp["asset"]["extensions"]["OpenMaterial_asset_info"]["asset_version"] = "1"
        j_temp["asset"]["extensions"]["OpenMaterial_asset_info"]["asset_variation"] = "1"
        j_temp["asset"]["extensions"]["OpenMaterial_asset_info"]["creator"] = self.return_creator()
        j_temp["asset"]["extensions"]["OpenMaterial_asset_info"]["description"] = "common road surface asphalt"
        j_temp["asset"]["extensions"]["OpenMaterial_asset_info"]["creation_date"] = self.return_time()
        # extensionsUsed

        # materials
        j_temp["materials"][0]["extensions"]["OpenMaterial_material_parameters"]["physical_properties"][
            "detection_wavelength_ranges"
        ][1]["min"] = 0.033
        j_temp["materials"][0]["extensions"]["OpenMaterial_material_parameters"]["physical_properties"][
            "detection_wavelength_ranges"
        ][1]["max"] = 0.037
        j_temp["materials"][0]["extensions"]["OpenMaterial_material_parameters"]["physical_properties"][
            "relative_permeability_uri"
        ] = ""  # os.path.join('data', '_'.join([name, 'permeability.gltf']))
        j_temp["materials"][0]["extensions"]["OpenMaterial_material_parameters"]["physical_properties"][
            "relative_permittivity_uri"
        ] = os.path.join("data", "_".join([name, "permittivity.gltf"]))
        j_temp["materials"][0]["name"] = name

        outfile_material_params_file = os.path.join(self.materialsDir, name + ".gltf")

        # check if valid
        json_schema_checker = self.schema.validateJsonViaSchema(self.schema.schema_material_params, j_temp)
        if json_schema_checker:
            with open(outfile_material_params_file, "w") as outfile_material_params:
                json.dump(j_temp, outfile_material_params, indent=4, sort_keys=True)
            print("finished writing material params ", name)
        else:
            print("Schema Check FAILED ", name)

    def fill_permittivity_json(self, name):
        """Add loaded raw data to permittivity json."""
        j_temp = copy.deepcopy(self.permittivity)
        uuid = self.return_uuid(name)
        # assets
        j_temp["asset"]["copyright"] = self.return_copyright()
        j_temp["asset"]["generator"] = self.return_generator()
        j_temp["asset"]["version"] = __version__
        j_temp["asset"]["extensions"]["OpenMaterial_asset_info"]
        j_temp["asset"]["extensions"]["OpenMaterial_asset_info"]["asset_type"] = "material"
        j_temp["asset"]["extensions"]["OpenMaterial_asset_info"]["id"] = uuid["uuid"].item()
        j_temp["asset"]["extensions"]["OpenMaterial_asset_info"]["title"] = " ".join(["Relative permittivity of", name])
        j_temp["asset"]["extensions"]["OpenMaterial_asset_info"]["asset_version"] = "1"
        j_temp["asset"]["extensions"]["OpenMaterial_asset_info"]["asset_variation"] = "1"
        j_temp["asset"]["extensions"]["OpenMaterial_asset_info"]["creator"] = self.return_creator()
        j_temp["asset"]["extensions"]["OpenMaterial_asset_info"]["description"] = " ".join(
            ["Relative permittivity of", name]
        )
        j_temp["asset"]["extensions"]["OpenMaterial_asset_info"]["creation_date"] = self.return_time()
        j_temp["asset"]["extensions"]["OpenMaterial_asset_info"]["sources"] = ""

        # data
        for i in range(len(j_temp["extensions"]["OpenMaterial_permittivity_data"]["data"][0]["permittivity"])):
            j_temp["extensions"]["OpenMaterial_permittivity_data"]["data"][0]["permittivity"].pop()

        # mat_name = [s for s in self.rawData.MaterialName if name in s]
        # j_tmp = self.rawData.RawDataEps.loc[self.rawData.RawDataEps["material"] == mat_name[0]]
        for index, row in self.rawData.RawDataEps.iterrows():
            j_temp["extensions"]["OpenMaterial_permittivity_data"]["data"][0]["permittivity"].append(
                [lightspeed / (row["!freq"] * 10e9), row["eps"], row["tand"]]
            )  # wavelength,eps

        filename = "_".join([name, "permittivity.gltf"])
        outfile_permittivity_file = os.path.join(self.materialsDir, "data", filename)

        # check if valid
        json_schema_checker = self.schema.validateJsonViaSchema(self.schema.schema_material_params, j_temp)
        if json_schema_checker:
            with open(outfile_permittivity_file, "w") as outfile_permittivity:
                json.dump(j_temp, outfile_permittivity, indent=4, sort_keys=True)
            print("finished writing permittivity params ", name)
        else:
            print("Schema Check FAILED ", name)

    def set_material_json(self, material):
        """Set the json file for basic material.

        Args:
            material (json): json like gltf file which includes the material properties
        """
        self.material_params = copy.deepcopy(material)

    def set_permittivity_json(self, permittivity):
        """Set the json file for permittivity.

        Args:
            permittivity (json): json like gltf file which includes the material properties
        """
        self.permittivity = copy.deepcopy(permittivity)

    def set_permeability_json(self, permeability):
        """Set the json file for permeability.

        Args:
            permeability (json): json like gltf file which includes the material properties
        """
        self.permeability = copy.deepcopy(permeability)


if __name__ == "__main__":
    OpenMaterial = open_material_data_set()
    print("successfully create Object")
    materials = OpenMaterial.get_material_names()
    print(materials)

    # iterate over list of names an generate the OpenMaterial database
    for material in materials:
        OpenMaterial.fill_json(material)

    print("Templates loaded")
