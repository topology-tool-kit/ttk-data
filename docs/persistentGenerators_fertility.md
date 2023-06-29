# Persistent Generators Fertility

![Persistent Generators Fertility example Image](https://topology-tool-kit.github.io/img/gallery/persistentGenerators_fertility.jpg)

## Pipeline description
This example computes the infinitely persistent 1-cycles of the surface.
These cycles smoothly capture the topological handles of the surface.

The surface generators are extracted using the eigenfunctions of the Laplace-Beltrami operator. These eigenfunctions are computed with [EigenField](https://topology-tool-kit.github.io/doc/html/classttkEigenField.html)
Generators are then computed on this smooth scalarfield using [PersistentGenerators](https://topology-tool-kit.github.io/doc/html/classttkPersistentGenerators.html).

Finally, the cycles are smoothed along the original surface using [SurfaceGeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkSurfaceGeometrySmoother.html)

The python script simply computes the cycles and saves the result as a .vtu file.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/persistentGenerators_fertility.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/persistentGenerators_fertility.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/persistentGenerators_fertility.py
```


## Inputs
- [fertility.vtu](https://github.com/topology-tool-kit/ttk-data/raw/dev/fertility.vtu): A 2-dimensionnal triangulation of the *fertility* dataset.

## Outputs
-  `PersistentGeneratorsFertility.vtu`: the infinitely persistent 1-cycles of the surface.


## C++/Python API

[EigenField](https://topology-tool-kit.github.io/doc/html/classttkEigenField.html)

[PersistentGenerators](https://topology-tool-kit.github.io/doc/html/classttkPersistentGenerators.html)

[SurfaceGeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkSurfaceGeometrySmoother.html)

