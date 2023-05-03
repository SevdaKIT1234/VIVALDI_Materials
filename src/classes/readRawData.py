"""readRawData.py.

Main script for converting KIT research and measurements into the OpenMaterial conform format.
This code is part of the VIVALDI public funded project.

Reading the raw data in and save is from excel
"""
import csv
import os

import matplotlib.pyplot as plt
import pandas as pd

__author__ = "Sandro Reith"
__project__ = "VIVALDI"
__copyright__ = "Copyright 2022, Continental AG"
__credits__ = ["Sandro Reith", "Sevda Abadpour"]
__version__ = "1.0.0"
__maintainer__ = "Sandro Reith"
__email__ = "sandro.reith@continental.com"
__status__ = "Production"


class raw_data_reader:
    """Read raw data."""

    def __init__(self):
        """Init class."""
        self.basePath = os.getcwd()
        self.RawDataEps = pd.DataFrame()
        self.MaterialName = []
        self.uuid = pd.DataFrame(columns=["material", "uuid"])
        self.Thickness = []
        self.RawPath = r"rawdata"
        self.TransfetPath = r"Transfering_Conti"
        self.read_raw_over_angle()
        self.read_raw_data_eps()
        self.read_uuid()

        print("The initialization for Openmaterial RawData is complete")

    def read_uuid(self):
        """ID uuid for every material name generated in advance by https://www.uuidgenerator.net/version4."""
        my_uuids = os.path.join(self.basePath, self.RawPath, "Data_Lookup_tables", "list_uuid.txt")
        self.uuid = pd.read_csv(my_uuids, sep=" ")
        print("Loaded uuids")

    def read_raw_over_angle(self):
        """Read s2p over angle from file."""
        myRawPath = os.path.join(
            self.basePath, self.RawPath, self.TransfetPath, "Reflectivity_Com_at_76-811_GHz_Scan_angle_-10.xlsx"
        )
        self.RawDataFreq = pd.read_excel(myRawPath)
        print("Loaded ", myRawPath)
        myRawPath = os.path.join(
            self.basePath, self.RawPath, self.TransfetPath, "Reflectivity_Com_at_78.5_GHz_Orginal.xlsx"
        )
        self.RawDataAngle = pd.read_excel(myRawPath)
        self.RawDataAngle = self.RawDataAngle.interpolate()
        print("Loaded ", myRawPath)

    def read_raw_data_eps(self):
        """Read permittivity from file."""
        # myRawPath=os.path.join(self.basePath, self.RawPath, "Data_Lookup_tables","SWISSto12 MCK", "data_20220519","Sample_Asphalt_58421AC8DS_19052022_1_eps.txt")
        datasets = []
        myRawPath = os.path.join(self.basePath, self.RawPath, "Data_Lookup_tables", "SWISSto12 MCK", "data_20220519")
        for fileRaw in os.listdir(myRawPath):
            if fileRaw.endswith(".txt"):
                fullFileRaw = os.path.join(myRawPath, fileRaw)
                # materialName = os.path.splitext(fileRaw)[0]
                dataset = pd.read_csv(fullFileRaw, sep=" ", skiprows=[0, 1, 2], index_col=False)
                with open(fullFileRaw) as fd:
                    reader = csv.reader(fd)
                    interestingrows = [row for idx, row in enumerate(reader) if idx in (1, 2)]
                flat_list = [item for sublist in interestingrows for item in sublist]
                flat_list = [s.replace("!", "") for s in flat_list]
                flat_list = [s.split("=") for s in flat_list]
                self.MaterialName.append(flat_list[0][1])
                self.Thickness.append(flat_list[1][1])
                datasets.append(dataset)
        # self.RawDataEps = pd.concat(datasets[name] for name in self.MaterialName)
        self.RawDataEps = pd.concat(d.assign(material=name) for name, d in zip(self.MaterialName, datasets))
        print("Loaded: ", self.MaterialName)

    def call_all_plot_raw_data(self):
        """Plot raw data."""
        self.plot_raw_freq()
        self.plot_raw_angle()
        self.plotRawEps()

    def plotRawEps(self):
        """Plot permittivity over freq."""
        plt.figure()
        # Names= self.RawDataEps.columns
        # for name in Names:
        # plt.plot(self.RawDataEps['!freq'], self.RawDataEps['eps'])
        for name in self.MaterialName:
            eps_temp = self.RawDataEps.loc[self.RawDataEps["material"] == name]
            plt.plot(eps_temp["!freq"], eps_temp["eps"])
        # plt.legend(Names)
        plt.legend(self.MaterialName)
        plt.xlabel("Frequency in GHz")
        plt.ylabel("Eps")
        plt.title("Permittivity Com at 75-90 GHz")
        # plt.title("Eps for ", self.MaterialName, " with Thickness=", self.Thickness, " mm")
        plt.show()
        print("Eps ", self.MaterialName)

    def plot_raw_angle(self):
        """Plot raw data over angle."""
        plt.figure()
        self.RawDataAngle.groupby("Scanning Angle")
        Name = self.RawDataAngle.columns[1:-1]
        for name in Name:
            plt.plot(self.RawDataAngle["Scanning Angle"], self.RawDataAngle[name])
        plt.legend(Name)
        plt.xlabel("Angle in Degree")
        plt.ylabel("S21 in dB")
        plt.title("Reflectivity Com at 78.5 GHz Scan angle=-90:90 Deg")
        plt.show()
        print("Angle")

    def plot_raw_freq(self):
        """Plot raw data over freq."""
        plt.figure()
        self.RawDataFreq.groupby("Frequency")
        Name = self.RawDataFreq.columns[1:-1]
        # Name = ['Asphalt (AC8DS)', 'Asphalt (PA8)', 'STL plate', 'Concrete', 'Wood','Radome']
        for name in Name:
            plt.plot(self.RawDataFreq["Frequency"], self.RawDataFreq[name])
        plt.legend(Name)
        plt.xlabel("Frequency in GHz")
        plt.ylabel("S21 in dB")
        plt.title("Reflectivity Com at 76-81 GHz Scan angle=-10 Deg")
        plt.show()
        print("Plot !")


if __name__ == "__main__":
    obj = raw_data_reader()
    obj.call_all_plot_raw_data()
    print("Finished Main Raw Reader")
