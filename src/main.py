"""
Main script for converting KIT research and measurements into the OpenMaterial conform format.
This code is part of the VIVALDI public funded project.
"""

import json
import os
import copy
from datetime import datetime
from classes.readerTemplate import OpenMaterialTemplate as Template
from classes.readRawData import RawDataReader as RawData

__author__ = "Sandro Reith"
__project__ = "VIVALDI"
__copyright__ = "Copyright 2022, Continental AG"
__credits__ = ["Sandro Reith", "Sevda Abadpour"]
__version__ = "1.0.0"
__maintainer__ = "Sandro Reith"
__email__ = "sandro.reith@continental.com"
__status__ = "Production"

class openMaterialDataSet(Template, RawData):
    """writting the OpenMaterial Output
    """
    def __init__(material, name):
        super()
        
        material.absolute_path = os.path.dirname(__file__)
        relativePathMaterials = "..\\materials"
        material.materialsDir = os.path.join(material.absolute_path, relativePathMaterials)
        
        material.name = name
        material.material_params = {}
        material.permeability = {}
        material.permittivity = {}
        material.Template = Template()
        material.rawData = RawData()

        material.initStructFromTemplate()
        material.fillMaterialJson(name)

    def initStructFromTemplate(self):
        """generate OpenMaterial Struct from Class
        """
        self.setMatirialJson(self.Template.material_params)
        self.setPermittivityJson(self.Template.permittivity)
        self.setPermeabilityJson(self.Template.permeability)

    def fillMaterialJson(self,name):
        """add loaded raw data to material json
        """
        tempJson=copy.deepcopy(self.material_params)
        tempJson["asset"]["copyright"]='(C) 2023, Karlsruhe Institute of Technology'
        tempJson["asset"]["generator"]="VIVALDI OpenMaterial Python Script"
        tempJson["asset"]["version"]="1.0"
        tempJson["asset"]["extensions"]["OpenMaterial_asset_info"]
        tempJson["asset"]["extensions"]["OpenMaterial_asset_info"]["asset_type"]="material"
        tempJson["asset"]["extensions"]["OpenMaterial_asset_info"]["id"] =  "0815"
        tempJson["asset"]["extensions"]["OpenMaterial_asset_info"]["title"] =  "_".join(["material", name])
        tempJson["asset"]["extensions"]["OpenMaterial_asset_info"]["asset_version"] =  "1"
        tempJson["asset"]["extensions"]["OpenMaterial_asset_info"]["asset_variation"] =  "1"
        tempJson["asset"]["extensions"]["OpenMaterial_asset_info"]["creator"] =  " Karlsruhe Institute of Technology and Continental AG"
        tempJson["asset"]["extensions"]["OpenMaterial_asset_info"]["description"] =  "common road surface asphalt"
        tempJson["asset"]["extensions"]["OpenMaterial_asset_info"]["creation_date"] =  datetime.now().strftime('%Y.%m.%d %H:%M:%S')
        
        outfile_material_params_file =  os.path.join(self.materialsDir, name+".gltf")
        with open(outfile_material_params_file, "w") as outfile_material_params:
            json.dump(tempJson, outfile_material_params,indent=4, sort_keys=True)
        print("finished writing material params ", name)

    def setMatirialJson(self, material):
        """set the json file for basic material

        Args:
            material (json): json like gltf file which includes the material properties
        """
        self.material_params = copy.deepcopy(material)
        
    def setPermittivityJson(self, permittivity):
        """set the json file for permittivity

        Args:
            permittivity (json): json like gltf file which includes the material properties
        """
        self.permittivity = copy.deepcopy(permittivity)

    def setPermeabilityJson(self, permeability):
        """set the json file for permeability

        Args:
            permeability (json): json like gltf file which includes the material properties
        """
        self.permeability = copy.deepcopy(permeability)

def main(dataset): 
    print("Loading material set: ", dataset)

if __name__ == "__main__":
    
    OpenMaterial = openMaterialDataSet("Asphalt_58421AC8DS")
    print("successfully create Object")

    # OpenMaterial.setMatirialJson(OpenMaterialTemplate.material_params)
    # OpenMaterial.setPermittivityJson(OpenMaterialTemplate.permittivity)
    # OpenMaterial.setPermeabilityJson(OpenMaterialTemplate.permeability)
    
    print("Templates loaded")

