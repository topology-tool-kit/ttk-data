# Persistence Clustering 3 Example

<!--[![Dragon example video tutorial](https://topology-tool-kit.github.io/img/gallery/dragon.jpg)](https://youtu.be/YVk9vRKIEX8)-->

<!--iframe width="100%" height="420"
src="https://www.youtube.com/embed/YVk9vRKIEX8" frameborder="0"
allowfullscreen></iframe-->

![Persistence Clustering 3 Image](https://topology-tool-kit.github.io/img/gallery/persistenceClustering3.jpeg)

## Pipeline description

This pipeline is similar to the previous ones.
<!--This example first loads a triangle mesh from disk.-->
First, this example loads a point cloud from disk (top left view in the above screenshot), then it computes a mesh on which a density field is obtained with a Gaussian Resampling on the points (top right view in the above screenshot). This density field will be considered as the input scalar data.
<!--In a pre-processing, the mesh is smoothed and an elevation function is computed on top of it.-->
<!--Then an elevation function is computed on it, and will be considered as the input scalar data for ou.-->

Next, a [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) is computed and thresholds are applied base on persistence to maintain only the features with a persistence above a certain value. The result is a simplified persistence diagram (bottom left view in the above screenshot).

The simplified persistence diagram is then used as a constraint for the [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html) of the input scalar data, giving us a simplified data.

Form there a [MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html) is computed (bottom right view in the above screenshot) then smoothed. Finally, by using the identifier of the 2-dimension cell of the Morse Smale complex where one point lands, a cluster is given to it.

<!--This simplified data is then used as the input of the computation of [ScalarFieldCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldCriticalPoints.html) (top left view, above screenshot) and the [ContourTree (FTM)](https://topology-tool-kit.github.io/doc/html/classttkFTMTree.html) (bottom left view, above screenshot).-->

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
$ paraview states/persistenceClustering3.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/persistenceClustering3.py"
```

## Inputs
- [clustering3.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/clustering3.csv): a table of 2 dimension points.

## Outputs
- `data3Resampled.csv`: the output is the data resampled in CSV file format.
<!-- `Segmentation.vtp`: the output Morse Smale complex in VTK file format (bottom right view, above screenshot).-->


## C++/Python API
[GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html)

[IcospheresFromPoints](https://topology-tool-kit.github.io/doc/html/classttkIcospheresFromPoints.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)

[MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html)
