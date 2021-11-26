# 1-Manifold Learning Circles example

![1-Manifold Learning Circles  example Image](https://topology-tool-kit.github.io/img/gallery/1manifoldLearningCircles.jpeg)

## Pipeline description


This example first loads a point cloud from disk. The points are arranged in mainly two concentric circles, one bigger than the other.

In a pre-processing, the data is converted to a format understandable by Paraview using the TableToPoints filter (upper left view, above screenshot). Gaussian Resampling is applied to the data. This filter has the effect of injecting input points to a structured data. For each injection, each point will "splat", or distribute values to nearby vertices. Only a slice of the data is kept (upper right, above screenshot). The data set is now represented by a density scalar field in 2D. 

Then, the [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) is computed and thresholds are applied base on persistence to maintain only the most persistent features. This results in a simplified persistence diagram (bottom left view, above screenshot).

The simplified persistence diagram is then used as a constraint for the [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html) of the input scalar data.

This simplified data is then used as the input of the computation of [MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttk_1_1MorseSmaleComplex.html) (bottom right view, above screenshot). This complex is composed of elements of 3 dimensions: dimension 0, which corresponds to the critical points of the Morse-Smale Complex, dimension 1, which corresponds to its edges and dimension 2, which corresponds to its surfaces. The edges of the Morse-Smale Complex will be situated in areas of highest and lowest densities, therefore it is possible to use them to outline the contour of the circles and assign each point to one.

## ParaView
To reproduce the above screenshot, go to your `ttk-data`  directory and enter the following command:
``` bash
$ paraview states/1manifoldLearningCircles.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/1manifoldLearningCircles.py"
```

## Inputs
- - [clustering0.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/clustering0.csv): a table containing 2D point coordinates arranged in concentric circles.

## Outputs
- `PersistenceDiagram.vtu`: the output persistence diagram in VTK file format (bottom left view, above screenshot). You are free to change the `vtu` file extension to that of any other supported file format (e.g. `csv`) in the above python script.
- `MorseComplexCriticalPoints.vtp`: the output critical points (or 0 dimensional elements) of the Morse Smale Complex in VTK file format (bottom right view, above screenshot). You are free to change the `vtp` file extension to that of any other supported file format (e.g. `csv`) in the above python script.
- `MorseComplex1Separatrices.vtp`: cylinders, representing the edges (or 1 dimensional elements) of the output Morse Smale Complex in VTK file format (bottom right view, above screenshot). You are free to change the `vtp` file extension to that of any other supported file format (e.g. `csv`) in the above python script.
- `MorseComplexSegmentation.vtp`: surfaces, representing the segmentation  of the output Morse Smale Complex in VTK file format (bottom right view, above screenshot). You are free to change the `vtp` file extension to that of any other supported file format (e.g. `csv`) in the above python script.

## C++/Python API

[GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html)

[MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttk_1_1MorseSmaleComplex.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)