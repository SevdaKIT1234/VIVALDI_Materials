# rawdata

The result of the data processed according to the OpenMATERIAL format.

| Filepath  | Description |
| ------------- | ------------- |
| [rawdata](.) | All inputfiles measured and processed from KIT. In these measurements, everything related to permitivity and s-parameters is considered raw data.
 |
| [data_20220519](./data_20220519) | The measured raw data of the quasi-optical bench as s-parameters (*.s2p) and the resulting permittivity (*.txt). |
| [meas](./meas) | Prepared [raw data](./data_20220519) as a stored dataframe. The raw data files were summarized and stored in an excel format. |
| [list_uuid.txt](./list_uuid) | Unique ID linked to the material names. |