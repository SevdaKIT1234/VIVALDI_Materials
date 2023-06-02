# rawdata

The result of the data processed according to the OpenMATERIAL format.
The data were measured on a quasi optical bench [Fig. 1](Fig-1). In this case, we understand [raw data](./data_20220519) to mean the dielectric properties of the DuT. The QoB is used to extract the s-parameters and then determine the permeability and permitivity from them. In OpenMATERIAL the permitivity and permeability are listed, for the sake of completeness the measured s-parameters are also listed here in the raw data.

<img align="left" width="256" height="256" src=../setup/QoB-setup.jpg>
Fig 1: The Image shows the KIT QoB setup. The DuT is attached to the table (*Rotating Probe Station*). The *Tx-atenna* is mounted in fixed position, whereby the *Rx-antenna* can move its position. The *Rx-antenna* can change the position over $\varphi_{Rx}$. Both antennas are connected to the Vecotr Network Analyser (*VNA*), where the s-parameters are recorded. The *PC* visualizes the measurement results and saves the *.s2p files, which are also available in the [data](./data_20220519) folder. 
<br/><br/>

| Filepath  | Description |
| ------------- | ------------- |
| [rawdata](.) | All inputfiles measured and processed from KIT. In these measurements, everything related to permitivity and s-parameters is considered raw data.|
| [data_20220519](./data_20220519) | The measured raw data of the quasi-optical bench as s-parameters (*.s2p) and the resulting permittivity (*.txt). |
| [meas](./meas) | Prepared [raw data](./data_20220519) as a stored dataframe. The raw data files were summarized and stored in an excel format. The name contains the date of measurement. |
| [list_uuid.txt](./list_uuid) | Unique ID linked to the material names. |
