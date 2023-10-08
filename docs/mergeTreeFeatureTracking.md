# Merge Tree Feature Tracking

![Merge Tree Feature Tracking example Image](https://topology-tool-kit.github.io/img/gallery/mergeTreeFeatureTracking.jpg)

## Pipeline description
This example first loads two pairs of timesteps of an ensemble of scalar fields inside a cinema database from disk.

Then, the [MergeTree](https://topology-tool-kit.github.io/doc/html/classttkMergeTree.html) is computed on each scalar field for the Split Tree.

These two pairs of timesteps are given respectively to two [MergeTreeClustering](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeClustering.html) filters to compute a distance between them.

In terms of visualisation, the matching between the trees of the first pair and the trees of the second pair are visualized using their planar layout and their embedding in the data.

The python script computes the matchings and saves the result (for each pair of trees).

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/mergeTreeFeatureTracking.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/mergeTreeFeatureTracking.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/mergeTreeFeatureTracking.py
```

## Inputs
- [Isabel.cdb](https://github.com/topology-tool-kit/ttk-data/tree/dev/Isabel.cdb): a cinema database containing 12 regular grids.

## Outputs
-  `matching_T2_T32.vtm`: the output matching between timestep 2 and 32.
-  `matching_T32_T45.vtm`: the output matching between timestep 32 and 45.


## C++/Python API
[BlockAggregator](https://topology-tool-kit.github.io/doc/html/classttkBlockAggregator.html)

[CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html)

[CinemaQuery](https://topology-tool-kit.github.io/doc/html/classttkCinemaQuery.html)

[CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html)

[MergeTree](https://topology-tool-kit.github.io/doc/html/classttkMergeTree.html)

[MergeTreeClustering](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeClustering.html)

