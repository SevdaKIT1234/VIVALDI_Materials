"""
Main script for converting KIT research and measurements into the OpenMaterial conform format.
This code is part of the VIVALDI public funded project.

Reading the raw data in and save is from excel
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import csv

__author__ = "Sandro Reith"
__project__ = "VIVALDI"
__copyright__ = "Copyright 2022, Continental AG"
__credits__ = ["Sandro Reith", "Sevda Abadpour"]
__version__ = "1.0.0"
__maintainer__ = "Sandro Reith"
__email__ = "sandro.reith@continental.com"
__status__ = "Production"

class RawDataReader():
    """read raw data
    """
    def __init__(self):
        self.basePath=os.getcwd()
        self.RawPath=r"rawdata"
        self.TransfetPath=r"Transfering_Conti"
        self.readRawOverAngle()
        self.readRawDataEps()
        print("The initialization for Openmaterial RawData is complete")

    def readRawOverAngle(self):
        myRawPath=os.path.join(self.basePath, self.RawPath, self.TransfetPath, "Reflectivity_Com_at_76-811_GHz_Scan_angle_-10.xlsx")
        self.RawDataFreq = pd.read_excel(myRawPath)
        print("Loaded ", myRawPath)
        myRawPath=os.path.join(self.basePath, self.RawPath, self.TransfetPath, "Reflectivity_Com_at_78.5_GHz_Orginal.xlsx")
        self.RawDataAngle = pd.read_excel(myRawPath)
        self.RawDataAngle = self.RawDataAngle.interpolate()
        print("Loaded ", myRawPath)
        
    def readRawDataEps(self):
        myRawPath=os.path.join(self.basePath, self.RawPath, "Data_Lookup_tables","SWISSto12 MCK", "data_20220519","Sample_Asphalt_58421AC8DS_19052022_1_eps.txt")
        self.RawDataEps = pd.read_csv(myRawPath, sep=" ",  skiprows=[0,1,2], index_col=False)
        with open(myRawPath) as fd:
            reader=csv.reader(fd)
            interestingrows=[row for idx, row in enumerate(reader) if idx in (1,2)]
        flat_list = [item for sublist in interestingrows for item in sublist]
        flat_list = [s.replace('!','') for s in flat_list ]
        flat_list = [s.split('=') for s in flat_list ]
        self.MaterialName=flat_list[0][1]
        self.Thickness=flat_list[1][1]
   
        print("Loaded: ",  self.MaterialName)

    def plotRaw(self):
        self.plotRawFreq()
        self.plotRawAngle()
        self.plotRawEps()
                
    def plotRawEps(self):
        fig=plt.figure()
        # Names= self.RawDataEps.columns
        # for name in Names:
        plt.plot(self.RawDataEps['!freq'], self.RawDataEps['eps'])
        # plt.legend(Names)
        plt.xlabel("Frequency in GHz")
        plt.ylabel("Eps")
        # plt.title("Eps for ", self.MaterialName, " with Thickness=", self.Thickness, " mm")
        plt.show()
        print("Eps ", self.MaterialName)

    def plotRawAngle(self):
        fig=plt.figure()
        self.RawDataAngle.groupby('Scanning Angle')
        Name = self.RawDataAngle.columns[1:-1]
        #Name = ['Asphalt (AC8DS)', 'Asphalt (PA8)', 'STL plate', 'Concrete', 'Wood','Radome']
        for name in Name:
            plt.plot(self.RawDataAngle['Scanning Angle'],self.RawDataAngle[name])
        plt.legend(Name)
        plt.xlabel("Angle in Degree")
        plt.ylabel("S21 in dB")
        plt.title("Reflectivity Com at 78.5 GHz Scan angle=-90:90 Deg")
        plt.show()
        print("Angle")

    def plotRawFreq(self):
        fig=plt.figure()
        self.RawDataFreq.groupby('Frequency')
        Name = self.RawDataFreq.columns[1:-1]
        #Name = ['Asphalt (AC8DS)', 'Asphalt (PA8)', 'STL plate', 'Concrete', 'Wood','Radome']
        for name in Name:
            plt.plot(self.RawDataFreq['Frequency'],self.RawDataFreq[name])
        plt.legend(Name)
        plt.xlabel("Frequency in GHz")
        plt.ylabel("S21 in dB")
        plt.title("Reflectivity Com at 76-81 GHz Scan angle=-10 Deg")
        plt.show()
        print("Plot !")

if __name__ == "__main__":
    obj=RawDataReader();
    obj.plotRaw();