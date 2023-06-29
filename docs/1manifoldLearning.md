# 1-Manifold Learning 

![1-Manifold Learning example Image](https://topology-tool-kit.github.io/img/gallery/1manifoldLearning.jpeg)


## Pipeline description

This example first loads a point cloud from disk. 

In a pre-processing, the [DimensionReduction](https://topology-tool-kit.github.io/doc/html/classttkDimensionReduction.html) is used to reduce the dimension of the input to 2D points. The data is then converted to a format understandable by Paraview using the `TableToPoints` filter. `GaussianResampling` is applied to the data (upper left view in the above screenshot). This filter has the effect of injecting input points to a structured data. For each injection, each point will "splat", or distribute values to nearby vertices. The resulting `SplatterValues` field is a density estimation (with a Gaussian kernel) of the point cloud projected in 2D.

Then, the [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) of a slice of the obtained data is computed and thresholds are applied based on persistence to maintain only the most persistent features. This results in a simplified persistence diagram.

The simplified persistence diagram is then used as a constraint for the [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html) of the input scalar data.

This simplified data is then used as the input of the computation of [MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html) (right view, above screenshot). This complex is composed of elements of 3 dimensions: dimension 0, which corresponds to the critical points of the Morse-Smale Complex, dimension 1, which corresponds to its edges and dimension 2, which corresponds to its surfaces. Only certain maximal edges are displayed here: using thresholds, the edges connecting at least one critical point situated in the boundary are discarded. This way, the "S" shape made by the point cloud is outlined.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/1manifoldLearning.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/1manifoldLearning.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/1manifoldLearning.py
```

## Inputs
- [pointCloud.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/pointCloud.csv): a table containing point coordinates.

## Outputs
- `OutputArc.vtu`: edges (or 1 dimensional elements) of the output Morse Smale Complex that are not connected to any boundary critical point in VTK file format (right view, above screenshot). You are free to change the `vtp` file extension to that of any other supported file format (e.g. `csv`) in the above python script.


## C++/Python API

[DimensionReduction](https://topology-tool-kit.github.io/doc/html/classttkDimensionReduction.html)

[GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html)

[MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)

