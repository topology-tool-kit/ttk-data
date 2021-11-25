# Persistence Clustering 1 Example

<!--[![Dragon example video tutorial](https://topology-tool-kit.github.io/img/gallery/dragon.jpg)](https://youtu.be/YVk9vRKIEX8)-->

<!--iframe width="100%" height="420"
src="https://www.youtube.com/embed/YVk9vRKIEX8" frameborder="0"
allowfullscreen></iframe-->

![Persistence Clustering 1 Image](https://topology-tool-kit.github.io/img/gallery/persistenceClustering1.jpeg)

## Pipeline description
<!--This example first loads a triangle mesh from disk.-->
Firstly, this example loads a cloud of points from disk (top left view in the above screenshot), then computes a mesh on which a density field is obtained with a Gaussian Resampling on the points (top right view in the above screenshot) and will be considered as the input scalar data.
<!--In a pre-processing, the mesh is smoothed and an elevation function is computed on top of it.-->
<!--Then an elevation function is computed on it, and will be considered as the input scalar data for ou.-->

Next, a [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) is computed and thresholds are applied base on pair identifier to remove the diagonal, and on persistence to maintain only the features with a persistence above a certain value. The result is a simplified persistence diagram (bottom left view in the above screenshot).

The simplified persistence diagram is then used as a constraint for the [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html) of the input scalar data, giving us a simplified data.

Form there a [MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html) is computed (bottom right view in the above screenshot) then smoothed, and a clusterization of the space results from it.



<!--This simplified data is then used as the input of the computation of [ScalarFieldCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldCriticalPoints.html) (top left view, above screenshot) and the [ContourTree (FTM)](https://topology-tool-kit.github.io/doc/html/classttkFTMTree.html) (bottom left view, above screenshot).-->

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
$ paraview states/persistenceClustering1.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/persistenceClustering1.py"
```

## Inputs
- `clustering1.csv`: a table of 2 dimension points.

## Outputs
- `PersistenceDiagram.vtu`: the output persistence diagram in VTK file format (bottom left view, above screenshot).
- `Segmentation.vtp`: the output Morse Smale complex in VTK file format (bottom right view, above screenshot).


## C++/Python API
<!--[ContourTree (FTM)](https://topology-tool-kit.github.io/doc/html/classttkFTMTree.html)-->

[GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html)

[IcospheresFromPoints](https://topology-tool-kit.github.io/doc/html/classttkIcospheresFromPoints.html)

<!--[PersistenceCurve](https://topology-tool-kit.github.io/doc/html/classttkPersistenceCurve.html)-->

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[ScalarFieldCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldCriticalPoints.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)

[MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html)
