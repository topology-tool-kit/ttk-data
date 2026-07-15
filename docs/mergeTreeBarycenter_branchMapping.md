# Merge Tree Barycenter with Branch Mapping 

![Branch Mapping and Distance Matrix example Image](https://topology-tool-kit.github.io/img/gallery/mergeTreeBarycenter_branchMapping.jpg)

## Pipeline description
This example first loads a multi block of scalar fields from disk.
Then, the Split Tree is computed on each scalar field using the [MergeTree](https://topology-tool-kit.github.io/doc/html/classttkMergeTree.html) module.

All these trees are passed to [MergeTreeClustering](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeClustering.html). It computes the distance and corresponding mapping between the first two trees in the metric space of merge trees defined by the branch mapping distance (thus, the underlying metric to the branch mapping distance). The [MergeTreeClustering](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeClustering.html) module only computes one distance and one mapping because the actual barycenter computation is not possible with this metric.

In addition, a distance matrix for the input trees is computed with [MergeTreeDistanceMatrix](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeDistanceMatrix.html).

The python script computes the branch mapping distance and saves the resulting mapping as well as the distance matrix in form of a table. The paraview state file additionally renders the matrix as a heatmap.

## ParaView
To reproduce the above screenshots, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/mergeTreeBarycenter_branchMapping.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/mergeTreeBarycenter_branchMapping.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/mergeTreeBarycenter_branchMapping.py
```


## Inputs
- [outlier.vtm](https://github.com/topology-tool-kit/ttk-data/tree/dev/bdied_outlier/outlier.vtm): a vtk multiblock containing 10 regular grids.

## Outputs
-  `merge_tree_mapping.vtm`: the computed branch mapping as a vtk multiblock.
-  `distance_matrix.csv`: the distance matrix as a csv table.


## C++/Python API
[BlockAggregator](https://topology-tool-kit.github.io/doc/html/classttkBlockAggregator.html)

[MergeTree](https://topology-tool-kit.github.io/doc/html/classttkMergeTree.html)

[MergeTreeClustering](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeClustering.html)

[MergeTreeDistanceMatrix](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeDistanceMatrix.html)

