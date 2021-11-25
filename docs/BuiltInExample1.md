# Built in example 1

![Built in example 1 Image](https://topology-tool-kit.github.io/img/gallery/builtinExample1.jpg)

## Pipeline description
This example computes minima, maxima and the persistence diagram for 2D flow data.

First, the data is transformed and preprocessed. 

Then, the [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) and [PersistenceCurve](https://topology-tool-kit.github.io/doc/html/classttkPersistenceCurve.html) are computed and thresholds are applied to the diagram based on persistence to maintain only the most persistent features. 

The diagonal, critical points and persistence pairs of the diagram are then converted to tubes and spheres to obtain a nicer rendering (bottom right view, above screenshot).

Next, the input data is simplified based on the selected persistent features, via [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html) and the 2D domain is embedded into 3D space based on the scalar values.

Then, the [Critical Points](https://topology-tool-kit.github.io/doc/html/classttkCriticalPoints.html) of the simplified and warped data are computed. 

Finally, the minima and maxima are extracted from the critcal points.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
$ paraview states/BuiltInExample1.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/BuiltInExample1.py"
```

## Inputs
- [BuiltInExample1.vti](https://github.com/topology-tool-kit/ttk-data/raw/dev/BuiltInExample1.vti): a two-dimensional regular grid encoding flow magnitude of a Kármán vortex street.

## Outputs
- `minima.vtu`: the warped minima vertices in VTK file format (middle view, above screenshot).
- `maxima.vtu`: the warped maxima vertices in VTK file format (middle view, above screenshot).
- `warpedInput.vtu`: the warped and tetrahedralized scalar field in VTK file format (middle view, above screenshot).
- `PersistenceCurve.csv`: the output persistence curve (top right view, above screenshot).
- `PersistenceDiagram.vtu`: the output persistence diagram in VTK file format (bottom right view, above screenshot). You are free to change the `vtu` file extension to that of any other supported file format (e.g. `csv`) in the above python script.

## C++/Python API
[PersistenceCurve](https://topology-tool-kit.github.io/doc/html/classttkPersistenceCurve.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)

[Critical Points](https://topology-tool-kit.github.io/doc/html/classttkCriticalPoints.html)

