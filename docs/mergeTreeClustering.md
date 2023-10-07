# Merge Tree Clustering 

![Merge Tree Clustering example Image](https://topology-tool-kit.github.io/img/gallery/mergeTreeClustering.jpg)

## Pipeline description
This example first loads an ensemble of scalar fields inside a cinema database from disk.
Then, the [MergeTree](https://topology-tool-kit.github.io/doc/html/classttkMergeTree.html) is computed on each scalar field for the Join Tree and the Split Tree.

All these trees are passed to [MergeTreeClustering](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeClustering.html) to compute a clustering in the metric space of merge trees. Each input is considered as a tuple consisting of the Join Tree and the Split Tree of the corresponding scalar field. Each centroid is also a tuple of this kind and a distance between two tuples is the distance between their Join Tree plus the distance between their Split Trees.

Then, a distance matrix is computed with [MergeTreeDistanceMatrix](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeDistanceMatrix.html) with the input trees and the 3 centroids.

This distance matrix is used as input of [DimensionReduction](https://topology-tool-kit.github.io/doc/html/classttkDimensionReduction.html) to compute a MultiDimensional Scaling (MDS), performing a dimensionality reduction in 2D respecting the most the input distance matrix.

In terms of visualisation, the MDS result is visualized and colored by clustering assignment. The split trees centroids are visualized with a planar layout and also some fields of each cluster.

In the second layout, the star clustering is visualized, consisting of the input split trees grouped by cluster, with the centroid of the cluster in the middle.

The python script computes the MDS and saves the resulting 2D points (for input trees and centroids).

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
araview states/mergeTreeClustering.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/mergeTreeClustering.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/mergeTreeClustering.py
```


## Inputs
- [Isabel.cdb](https://github.com/topology-tool-kit/ttk-data/tree/dev/Isabel.cdb): a cinema database containing 12 regular grids.

## Outputs
-  `MDS_trees.vtu`: the output points in 2D MDS (MultiDimensional Scaling) corresponding to the input trees. The 'ClusterAssignment' array contains the clustering assignments.
-  `MDS_centroids.vtu`: the output points in 2D MDS (MultiDimensional Scaling) corresponding to the centroids.


## C++/Python API
[BlockAggregator](https://topology-tool-kit.github.io/doc/html/classttkBlockAggregator.html)

[CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html)

[CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html)

[DimensionReduction](https://topology-tool-kit.github.io/doc/html/classttkDimensionReduction.html)

[FlattenMultiBlock](https://topology-tool-kit.github.io/doc/html/classttkFlattenMultiBlock.html)

[MergeTree](https://topology-tool-kit.github.io/doc/html/classttkMergeTree.html)

[MergeTreeClustering](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeClustering.html)

[MergeTreeDistanceMatrix](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeDistanceMatrix.html)

