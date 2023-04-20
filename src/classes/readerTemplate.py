"""
Main script for converting KIT research and measurements into the OpenMaterial conform format.
This code is part of the VIVALDI public funded project.

Read OpenMaterial templates.
"""

import json as j
import os

__author__ = "Sandro Reith"
__project__ = "VIVALDI"
__copyright__ = "Copyright 2022, Continental AG"
__credits__ = ["Sandro Reith", "Sevda Abadpour"]
__version__ = "1.0.0"
__maintainer__ = "Sandro Reith"
__email__ = "sandro.reith@continental.com"
__status__ = "Production"

class OpenMaterialTemplate():
    """load the OpenMaterial template
    """
    def __init__(self):
        """init @OpenMaterial class
        """
        self.absolute_path = os.path.dirname(__file__)
        relative_path = "..\\template"
        self.templateDir = os.path.join(self.absolute_path, relative_path)
        self.material_params = {}
        self.permeability = {}
        self.permittivity = {}
        self.loadTemplates()
        print("The initialization for Openmaterial Template is complete")

    def loadTemplates(self):
        """load the templates from template folder
        """
        if os.path.isdir(self.templateDir):
            filenames = next(os.walk(self.templateDir), (None, None, []))[2]  # [] if no file
            for file in filenames:
                if file.__contains__("mymaterial.gltf"):
                    with open(os.path.join(self.templateDir, file), 'r') as f:
                        self.material_params = j.load(f)
                elif file.__contains__("permittivity.gltf"):
                    with open(os.path.join(self.templateDir, file), 'r') as f:
                        self.permittivity = j.load(f)
                elif file.__contains__("permeability.gltf"):
                    with open(os.path.join(self.templateDir, file), 'r') as f:
                        self.permeability = j.load(f)
                else:
                    print("Not used: ", file)
        else:
            print("EROOR::template folder is not available ", self.templateDir)

        def  getPermeabilityTemplate(self):
            return self.permeability

        def  getPermittivityTemplate(self):
            return self.permittivity

        def  getMaterialTemplate(self):
            return self.material_params

if __name__ == "__main__":
    obj = OpenMaterialTemplate()