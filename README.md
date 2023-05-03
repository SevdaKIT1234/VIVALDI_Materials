# VIVALDI OpenMaterial

This git repository contains the measured raw data and the generated OpenMaterial files of the VIVALDI project. In addition, code is stored with which the raw data can be viewed and the OpenMaterial files can be generated.
## VIVALDI

To this end, virtual test environments are being developed for the sensor systems that are of central importance for connected and automated driving. They are used to simulate the functions of sensors, the impact of the environment, and the representation of scenarios. Different approaches from software-in-the-loop over over-the-air vehicle-in-the-loop up to field-operational tests are pursued in combination. The project is investigating how close to reality such tests can be in a virtual environment and to what extent they can represent the actual complexity of test drives. The aim is to develop realistic models for scenarios, sensors and environments that will enable standardized test procedures. In cooperation with the Japanese partners of the DIVP consortium, complementary scientific approaches and central questions of modelling, simulation and validation are being worked on.

More information about the VIALDI project can be found on the [website](https://www.safecad-vivid.net/).

## OpenMaterial

OpenMaterial is a proposal that deals with how to exchange data for virtual validation and how to describe and structure this exchange. In the VIVALDI project, we had the same experience and therefore decided to use OpenMaterial. 

More information about the VIALDI project can be found on the [website](https://github.com/LudwigFriedmann/OpenMATERIAL).

## File Structure

| Filepath  | Description |
| ------------- | ------------- |
| [materials](./materials) | OpenMaterial output folder structer with the generated material files. |
| [rawdata](./rawdata) | Measured raw data ( s-Parameters and permittivity ) which serve as input for the [src](./src) code. |
| [src](./src) | The Python code. |
| [setup](./rawdata) | Files needed to build the environment. |