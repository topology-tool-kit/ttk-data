# Compact Triangulation 

<iframe width="100%" height="420"
src="https://www.youtube.com/embed/vDQRh_tuUSA" frameborder="0"
allowfullscreen></iframe>

## Pipeline description
This example first loads a triangle mesh from disk.
In a pre-processing, an elevation function along the y-axis is computed on top of the mesh.
The elevation function will be considered as the input scalar data in the remainder.

Then, the example uses [TriangulationManager](https://topology-tool-kit.github.io/doc/html/classttkTriangulationManager.html) to divide the input datasets into different clusters using Point Region (PR) [Octree](https://topology-tool-kit.github.io/doc/html/classOctree.html) with the parameter `Bucket threshold` being set `1000`. 
The clustering information is saved into a new scalar field named `ttkCompactTriangulationIndex`, and the number in the scalar field denotes the cluster index for each vertex. 

At this point, any TTK plugin to be applied will be executed with [CompactTriangulation](https://topology-tool-kit.github.io/doc/html/classttk_1_1CompactTriangulation.html). Notice that CompactTriangulation supports any clustering technique as long as it is vertex-based. To use any other clustering method, the dataset is required to include the `ttkCompactTriangulationIndex` scalar field, which stores the cluster index for each vertex. 

Finally, the example computes the [ScalarFieldCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldCriticalPoints.html) with the input scalar data generated with the elevation function. 

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview --state=states/compactTriangulation.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/compactTriangulation.py"
```

## Inputs
- [dragon.vtu](https://github.com/topology-tool-kit/ttk-data/raw/dev/dragon.vtu): a two-dimensional triangulation.

## Outputs
-  `CompactTriangulation.vtu`: the input dataset in VTK file format with an additional scalar field named `ttkCompactTriangulationIndex` that stores the clustering information.  
- `CriticalPoints.vtp`: the output critical points in VTK file format. You are free to change the `vtp` file extension to that of any other supported file format (e.g. `csv`) in the above python script.


## C++/Python API
[CompactTriangulation](https://topology-tool-kit.github.io/doc/html/classttk_1_1CompactTriangulation.html)

[TriangulationManager](https://topology-tool-kit.github.io/doc/html/classttkTriangulationManager.html)

[Octree](https://topology-tool-kit.github.io/doc/html/classOctree.html)

[ScalarFieldCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldCriticalPoints.html)
