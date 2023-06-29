# Compact Triangulation 

<iframe width="100%" height="420"
src="https://www.youtube.com/embed/vDQRh_tuUSA" frameborder="0"
allowfullscreen></iframe>

## Pipeline description
This example demonstrates how to invoke the [CompactTriangulation](https://topology-tool-kit.github.io/doc/html/classttk_1_1CompactTriangulation.html) data structure in TTK. 

The example first loads a triangle mesh from disk. An elevation function along the y-axis is then computed and added on top of the mesh using the `Elevation` filter.

Then, the example uses [TriangulationManager](https://topology-tool-kit.github.io/doc/html/classttkTriangulationManager.html) to initialize a clustering of the mesh vertices. The clustering information is saved into a new scalar field named `ttkCompactTriangulationIndex`. The number associated with each vertex by `ttkCompactTriangulationIndex` represents the cluster index to which the vertex belongs.

Once a scalar field named `ttkCompactTriangulationIndex` is defined on a dataset, any TTK plugin applied to such dataset will be executed using the `CompactTriangulation` data structure.

The example continues applying the [ScalarFieldCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldCriticalPoints.html) module on the elevation function previously defined on the input mesh.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/compactTriangulation.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/compactTriangulation.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/compactTriangulation.py
```


## Inputs
- [dragon.vtu](https://github.com/topology-tool-kit/ttk-data/raw/dev/dragon.vtu): a two-dimensional triangulation.

## Outputs
-  `CompactTriangulation.vtu`: the input dataset in VTK file format with an additional scalar field named `ttkCompactTriangulationIndex` that stores the cluster index for each vertex.  
- `CriticalPoints.vtp`: the output critical points in VTK file format. You are free to change the `vtp` file extension to that of any other supported file format (e.g. `csv`) in the above python script.


## C++/Python API
[CompactTriangulation](https://topology-tool-kit.github.io/doc/html/classttk_1_1CompactTriangulation.html)

[TriangulationManager](https://topology-tool-kit.github.io/doc/html/classttkTriangulationManager.html)

[Octree](https://topology-tool-kit.github.io/doc/html/classOctree.html)

[ScalarFieldCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldCriticalPoints.html)
