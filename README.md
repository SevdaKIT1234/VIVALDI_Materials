# VIVALDI Materials

This git repository contains the measured raw data and the generated OpenMATERIAL files of the VIVALDI funded project. In addition, code is stored with which the raw data can be viewed and the OpenMATERIAL files can be generated.

The repo contains extensive measurements in the mmWave range.
In the quasi-optical bench, various materials were measured with a vector analyser and the scattering  parameters were recorded.
In addition, the complex permitivity $\epsilon_r$. 
and permeability $\mu_r$ were calculated from the s-parameters, as these are the physical quantities that are most commonly used. As a small addition, only non-metallic or non-magnetic materials are used here, so the permeability can be assumed to be  $\mu_r = 1 \frac{H}{m}$ or $\mu_r = 1 - 0.00001j \frac{H}{m}$, which significantly simplifies the calculation of permittivity $\epsilon_r$.

## VIVALDI

To this end, virtual test environments are being developed for the sensor systems that are of central importance for connected and automated driving. They are used to simulate the functions of sensors, the impact of the environment, and the representation of scenarios. Different approaches from software-in-the-loop over over-the-air vehicle-in-the-loop up to field-operational tests are pursued in combination. The project is investigating how close to reality such tests can be in a virtual environment and to what extent they can represent the actual complexity of test drives. The aim is to develop realistic models for scenarios, sensors and environments that will enable standardized test procedures. In cooperation with the Japanese partners of the DIVP consortium, complementary scientific approaches and central questions of modelling, simulation and validation are being worked on.

More information about the VIALDI project can be found on the [website](https://www.safecad-vivid.net/).

## OpenMATERIAL

OpenMATERIAL is a proposal that deals with how to exchange data for virtual validation and how to describe and structure this exchange. In the VIVALDI project, we had the same experience and therefore decided to use OpenMATERIAL. 

More information about the OpenMATERIAL project can be found on the [website](https://github.com/LudwigFriedmann/OpenMATERIAL).

## File Structure

| Filepath  | Description |
| ------------- | ------------- |
| [materials](./materials) | OpenMATERIAL output folder structer with the generated material files. |
| [rawdata](./rawdata) | Measured raw data ( s-Parameters and permittivity ) which serve as input for the [src](./src) code. |
| [src](./src) | The Python code. |
| [setup](./rawdata) | Files needed to build the environment. |
