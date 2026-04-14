# Merge Tree Principal Geodesic Analysis 

![Merge Tree Principal Geodesic Analysis example Image](https://topology-tool-kit.github.io/img/gallery/mergeTreePGA.jpg)


## Pipeline description
This example first loads an ensemble of scalar fields inside a cinema database from disk.
Then, the [MergeTree](https://topology-tool-kit.github.io/doc/html/classttkMergeTree.html) is computed on each scalar field to compute the Split Tree.

All these trees are passed to [MergeTreePrincipalGeodesics](https://topology-tool-kit.github.io/doc/html/classttkMergeTreePrincipalGeodesics.html) to compute principal geodesic analysis in the metric space of merge trees. 

Then the filter [MergeTreePrincipalGeodesicsDecoding](https://topology-tool-kit.github.io/doc/html/classttkMergeTreePrincipalGeodesicsDecoding.html) is used to reconstruct the input trees, to sample evenly trees along the principal geodesics and to sample a discrete grid of merge trees of the PGA basis.

A distance matrix is then computed with [MergeTreeDistanceMatrix](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeDistanceMatrix.html) with the trees of the grid. This distance matrix is used as input of [DimensionReduction](https://topology-tool-kit.github.io/doc/html/classttkDimensionReduction.html) to compute a MultiDimensional Scaling (MDS), performing a dimensionality reduction in 3D (and 2D with a second DimensionReduction filter) respecting the most the input distance matrix. 

Finally the [PointSetToSurface](https://topology-tool-kit.github.io/doc/html/classttkPointSetToSurface.html) and [ProjectionFromTable](https://topology-tool-kit.github.io/doc/html/classttkProjectionFromTable.html) are used to create the 3D surface (and the 2D surface). The ProjectionFromTable allows to project the points (reconstructed trees, geodesic trees etc.) to the 3D (or 2D) surface.

In terms of visualisation, a scalar field of each cluster is displayed with a zoom on their right of the important persistence pairs. The original trees are displayed alongside their reconstruction at their right. The persistence pairs of the trees are colored by ID to see what features they correspond to in the scalar field.

The 3D and 2D surface are displayed with the persistence correlation view at the top right. The 12 scalar fields are colored by Cluster ID. Finally, a path drawn with PolyLineSource on the surface is drawn at the bottom right to show how we can interactivily explore the MT-PGA basis in user-defined locations.

The python script computes the MT-PGA basis. It saves the resulting coefficients of the input trees and the geodesics of the basis. Finally it saves the reconstructed trees given the basis and the coordinates of the trees in the basis.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/mergeTreePGA.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/mergeTreePGA.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/mergeTreePGA.py
```

## Inputs
- [Earthquake.cdb](https://github.com/topology-tool-kit/ttk-data/tree/dev/Earthquake.cdb): a cinema database containing 12 regular grids.

## Outputs
-  `MT-PGA_coef.csv`: the coefficients of the input trees corresponding to their coordinates in the PGA basis.
-  `MT-PGA_geodesics.csv`: the geodesics of the PGA basis.
-  `MT-PGA_reconstructed_trees.vtm`: the reconstructed input trees.


## C++/Python API
[BlockAggregator](https://topology-tool-kit.github.io/doc/html/classttkBlockAggregator.html)

[CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html)

[CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html)

[DataSetToTable](https://topology-tool-kit.github.io/doc/html/classttkDataSetToTable.html)

[DimensionReduction](https://topology-tool-kit.github.io/doc/html/classttkDimensionReduction.html)

[FlattenMultiBlock](https://topology-tool-kit.github.io/doc/html/classttkFlattenMultiBlock.html)

[MergeTree](https://topology-tool-kit.github.io/doc/html/classttkMergeTree.html)

[GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html)

[MergeBockTables](https://topology-tool-kit.github.io/doc/html/classttkMergeBockTables.html)

[MergeTreeClustering](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeClustering.html)

[MergeTreeDistanceMatrix](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeDistanceMatrix.html)

[MergeTreePrincipalGeodesics](https://topology-tool-kit.github.io/doc/html/classttkMergeTreePrincipalGeodesics.html)

[MergeTreePrincipalGeodesicsDecoding](https://topology-tool-kit.github.io/doc/html/classttkMergeTreePrincipalGeodesicsDecoding.html)

[PointSetToCurve](https://topology-tool-kit.github.io/doc/html/classttkPointSetToCurve.html)

[PointSetToSurface](https://topology-tool-kit.github.io/doc/html/classttkPointSetToSurface.html)

[ProjectionFromTable](https://topology-tool-kit.github.io/doc/html/classttkProjectionFromTable.html)
