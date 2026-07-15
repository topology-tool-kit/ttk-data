# Merge Tree Barycenter with Path Mapping 

![Path Mapping Barycenter and Distance Matrix example Image](https://topology-tool-kit.github.io/img/gallery/mergeTreeBarycenter_pathMapping.jpg)

## Pipeline description
This example first loads a multi block of scalar fields from disk.
Then, the Split Tree is computed on each scalar field using the [MergeTree](https://topology-tool-kit.github.io/doc/html/classttkMergeTree.html) module.

All these trees are passed to [MergeTreeClustering](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeClustering.html) to compute a barycenter in the metric space of merge trees defined by the path mapping distance (thus, the number of clusters has to be set to one and the underlying metric to the path mapping distance). 

In addition, a distance matrix for the input trees is computed with [MergeTreeDistanceMatrix](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeDistanceMatrix.html).

The python script computes the barycenter and saves the resulting planar layout as well as the distance matrix in form of a table. The paraview state file additionally renders the matrix as a heatmap.

## ParaView
To reproduce the above screenshots, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/mergeTreeBarycenter_pathMapping.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/mergeTreeBarycenter_pathMapping.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/mergeTreeBarycenter_pathMapping.py
```


## Inputs
- [outlier.vtm](https://github.com/topology-tool-kit/ttk-data/tree/dev/bdied_outlier/outlier.vtm): a vtk multiblock containing 10 regular grids.

## Outputs
-  `merge_tree_barycenter.vtm`: the computed barycenter merge tree as a vtk multiblock.
-  `distance_matrix.csv`: the distance matrix as a csv table.


## C++/Python API
[BlockAggregator](https://topology-tool-kit.github.io/doc/html/classttkBlockAggregator.html)

[MergeTree](https://topology-tool-kit.github.io/doc/html/classttkMergeTree.html)

[MergeTreeClustering](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeClustering.html)

[MergeTreeDistanceMatrix](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeDistanceMatrix.html)

