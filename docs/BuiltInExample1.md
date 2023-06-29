# Builtin example 1

![Built in example 1 Image](https://topology-tool-kit.github.io/img/gallery/builtinExample1.jpg)

## Pipeline description
This example computes minima, maxima and the persistence diagram for 2D flow data (von Karman vortex street).

First, the data is transformed and preprocessed to estimate the vorticity of the flow (via the orthogonal component of the curl). 

Then, the [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) and [PersistenceCurve](https://topology-tool-kit.github.io/doc/html/classttkPersistenceCurve.html) are computed.
To the persistence diagram, a threshold is applied to remove the diagonal.
The output are the persistence pairs.
These pairs are filtered based on persistence to maintain only the most persistent features.

Next, the input data is simplified based on the selected persistent features, via [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html) and the 2D domain is embedded into 3D space based on the scalar values.

Finally, the [Critical Points](https://topology-tool-kit.github.io/doc/html/classttkCriticalPoints.html) of the simplified and warped data are computed.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/BuiltInExample1.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/BuiltInExample1.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/BuiltInExample1.py
```

## Inputs
- [BuiltInExample1.vti](https://github.com/topology-tool-kit/ttk-data/raw/dev/BuiltInExample1.vti): a two-dimensional regular grid encoding flow magnitude of a Kármán vortex street.

## Outputs
- `warpedInput.vtu`: the warped and tetrahedralized scalar field in VTK file format (middle view, above screenshot).
- `CriticalPoints.csv`: the critical points of the warped scalar field in csv format (middle view, above screenshot).
- `PersistenceCurve.csv`: the output persistence curve (top right view, above screenshot).
- `PersistenceDiagram.vtu`: the output persistence diagram in VTK file format (bottom right view, above screenshot). You are free to change the `vtu` file extension to that of any other supported file format (e.g. `csv`) in the above python script.

## C++/Python API
[PersistenceCurve](https://topology-tool-kit.github.io/doc/html/classttkPersistenceCurve.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[ScalarFieldCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkCriticalPoints.html)

[ScalarFieldSmoother](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldSmoother.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)


