# Persistent Generators DarkSky

![Persistent Generators DarkSky example Image](https://topology-tool-kit.github.io/img/gallery/persistentGenerators_darkSky.jpg)

## Pipeline description
This example computes the most persistent one-dimensional generators of the opposite of the density of dark matter in an astrophysics simulation.
These generators characterize prominent loops in the *cosmic web*.

The data is originally a point cloud. It is processed into a scalar field defined on a regular grid using Gaussian resampling.

Generators are then computed using [PersistentGenerators](https://topology-tool-kit.github.io/doc/html/persistentGenerators.html), and thresholded
in order to keep the most persistent ones..

For context, the one-dimensional separatrices of the MorseSmale complex are
computed using [MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html) after some topological
simplification using [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)and shown in the ParaView example.


The python script simply computes the most persistent generators and saves the result as a .vtu file.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/persistentGenerators_darkSky.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/persistentGenerators_darkSky.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/persistentGenerators_darkSky.py
```


## Inputs
- [ds14_scivis_0128_e4_dt04_1.0000.vtp](https://github.com/topology-tool-kit/ttk-data/raw/dev/ds14_scivis_0128_e4_dt04_1.0000.vtp): A point cloud dataset representing a simulation of the density of dark matter in the universe.

## Outputs
-  `PersistentGeneratorsDarkSky.vtu`: the raw one-dimensional most persistent generators of the field.


## C++/Python API

[MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html)

[PersistentGenerators](https://topology-tool-kit.github.io/doc/html/classttkPersistentGenerators.html)

[ScalarFieldSmoother](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldSmoother.html)

