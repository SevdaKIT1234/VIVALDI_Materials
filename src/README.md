# src

Here are all pyhton files of the project. The main file is the [main.py](./main.py).
The main file creates an object, reads the raw data and creates the output in OpenMATERIAL format.
In [template](./template) folder, the schema files can be found and a default OpenMATERIAL file from which the struct is adopted.

To create the OpenMATERIAL files you have to run the [main.py](./main.py) then the data is written to the materials folder.


```console
(v_openmaterial) user@pc: python main.py
```

To create the plots, the script [readerRawData.py](./classes/readRawData.py) can be executed under class. It can be found in [classes](./classes/) folder.

| Filepath  | Description |
| ------------- | ------------- |
| [classes](./classes) | Classes for the main script. Every Class can be executed by itself. |
| [template](./template) | Templates for OpenMaterial. |
| [main.py](./main.py) | Entry file. |