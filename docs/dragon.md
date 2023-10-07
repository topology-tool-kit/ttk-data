# Dragon 

<!--[![Dragon example video tutorial](https://topology-tool-kit.github.io/img/gallery/dragon.jpg)](https://youtu.be/YVk9vRKIEX8)-->

<iframe width="100%" height="420"
src="https://www.youtube.com/embed/YVk9vRKIEX8" frameborder="0"
allowfullscreen></iframe>

## Pipeline description
This example first loads a triangle mesh from disk.
In a pre-processing, the mesh is smoothed and an elevation function is computed on top of it.
The elevation function will be considered as the input scalar data in the remainder.

Then, the [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) is computed and thresholds are applied base on persistence to maintain only the most persistent features. This results in a simplified persistence diagram (bottom right view in the above screenshot).

The [PersistenceCurve](https://topology-tool-kit.github.io/doc/html/classttkPersistenceCurve.html) is also computed (top right view in the above screenshot).

The simplified persistence diagram is then used as a constraint for the [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html) of the input scalar data.

This simplified data is then used as the input of the computation of [ScalarFieldCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldCriticalPoints.html) (top left view, above screenshot) and the [ContourTree](https://topology-tool-kit.github.io/doc/html/classttkContourTree.html) (bottom left view, above screenshot).

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/dragon.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/dragon.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/dragon.py
```


## Inputs
- [dragon.vtu](https://github.com/topology-tool-kit/ttk-data/raw/dev/dragon.vtu): a two-dimensional triangulation.

## Outputs
- `PersistenceDiagram.vtu`: the output persistence diagram in VTK file format (bottom right view, above screenshot). You are free to change the `vtu` file extension to that of any other supported file format (e.g. `csv`) in the above python script.
- `PersistenceCurve.csv`: the output persistence curve.
- `CriticalPoints.vtp`: the output
critical points
in VTK file format (bottom right view, above screenshot). You are free to change the `vtp` file extension to that of any other supported file format (e.g. `csv`) in the above python script.
- `ContourTreeNode.vtp`: spheres, representing the nodes of the output contour tree
in VTK file format (bottom right view, above screenshot). You are free to change the `vtp` file extension to that of any other supported file format (e.g. `csv`) in the above python script.
- `ContourTreeArcs.vtp`: cylinders, representing the arcs of the output contour tree
in VTK file format (bottom right view, above screenshot). You are free to change the `vtp` file extension to that of any other supported file format (e.g. `csv`) in the above python script.


## C++/Python API
[ContourTree](https://topology-tool-kit.github.io/doc/html/classttkContourTree.html)

[GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html)

[IcospheresFromPoints](https://topology-tool-kit.github.io/doc/html/classttkIcospheresFromPoints.html)

[PersistenceCurve](https://topology-tool-kit.github.io/doc/html/classttkPersistenceCurve.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[ScalarFieldCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldCriticalPoints.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)

