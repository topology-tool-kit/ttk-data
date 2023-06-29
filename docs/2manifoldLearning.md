# 2-Manifold Learning 

![2-Manifold Learning example Image](https://topology-tool-kit.github.io/img/gallery/2manifoldLearning.jpeg)


## Pipeline description

This example first loads a point cloud from disk. 

In a pre-processing, the data is converted to a format understandable by Paraview using the `TableToPoints` filter. `GaussianResampling` is applied to the data (left view in the above screenshot). This filter has the effect of injecting input points to a structured data. For each injection, each point will "splat", or distribute values to nearby vertices. The resulting scalar field is a density estimation (with a Gaussian kernel) of the input point cloud.

Then, the [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) is computed and thresholds are applied based on persistence to maintain only the most persistent features. This results in a simplified persistence diagram.

The simplified persistence diagram is then used as a constraint for the [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html) of the input scalar data.

This simplified data is then used as the input of the computation of [MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html) (right view, above screenshot). This complex is composed of elements of 4 dimensions: dimension 0, which corresponds to the critical points of the Morse-Smale Complex, dimension 1, which corresponds to its edges (in grey in the screenshot) and dimension 2, which corresponds to its surfaces, and dimension 3, which corresponds to pieces of volume that can be extracted from the `Segmentation` output. The "S" shape made by the point cloud is outlined by the maximal 1 and 2 dimension elements of the Morse-Smale Complex.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/2manifoldLearning.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/2manifoldLearning.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/2manifoldLearning.py
```


## Inputs
- [pointCloud.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/pointCloud.csv): a table containing point coordinates.

## Outputs
- `OutputSurface.vtu`: surface (or 2 dimensional elements) of the output Morse Smale Complex in VTK file format (right view, above screenshot). You are free to change the `vtp` file extension to that of any other supported file format (e.g. `csv`) in the above python script.


## C++/Python API

[GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html)

[MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)

