# Persistence Diagram Principal Geodesic Analysis 

![Persistence Diagram Principal Geodesic Analysis example Image]()

## Pipeline description
This example first loads an ensemble of scalar fields inside a cinema database from disk.
Then, the [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) is computed on each scalar field.

All these diagrams are passed to [MergeTreePrincipalGeodesics](https://topology-tool-kit.github.io/doc/html/classttkMergeTreePrincipalGeodesics.html) to compute principal geodesic analysis in the metric space of persistence diagrams. 

Then the filter [MergeTreePrincipalGeodesicsDecoding](https://topology-tool-kit.github.io/doc/html/classttkMergeTreePrincipalGeodesics.html) is used to reconstruct the input diagrams, to sample evenly diagrams along the principal geodesics and to sample a discrete grid of persistence diagrams of the PGA basis. 

A distance matrix is then computed with [MergeTreeDistanceMatrix](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeDistanceMatrix.html) with the diagrams of the grid. This distance matrix is used as input of [DimensionReduction](https://topology-tool-kit.github.io/doc/html/classttkDimensionReduction.html) to compute a MultiDimensional Scaling (MDS), performing a dimensionality reduction in 3D (and 2D with a second DimensionReduction filter) respecting the most the input distance matrix. 

Finally the [PointSetToSurface](https://topology-tool-kit.github.io/doc/html/classttkPointSetToGrid.html) and [ProjectionFromTable](https://topology-tool-kit.github.io/doc/html/classttkProjectionFromTable.html) are used to create the 3D surface (and the 2D surface). The ProjectionFromTable allows to project the points (reconstructed diagrams, geodesic diagrams etc.) to the 3D (or 2D) surface.

In terms of visualisation, a scalar field of each cluster is displayed. The original diagrams are displayed alongside their reconstruction at their right. The persistence pairs of the diagrams are colored by ID to see what features they correspond to in the scalar field.

The 3D and 2D surface are displayed with the persistence correlation view at the right. The 12 scalar fields are colored by Cluster ID. 

The python script computes the PD-PGA and saves the resulting coefficients of the input diagrams.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
$ paraview --state=states/persistenceDiagramPGA.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/persistenceDiagramPGA.py"
```

## Inputs
- [Isabel.cdb](https://github.com/topology-tool-kit/ttk-data/tree/dev/Isabel.cdb): a cinema database containing 12 regular grids.

## Outputs
-  `PD-PGA_coef.csv`: the coefficients of the input diagrams corresponding to their coordinates in the PGA basis.


## C++/Python API
[BlockAggregator](https://topology-tool-kit.github.io/doc/html/classttkBlockAggregator.html)

[CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html)

[CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html)

[DataSetToTable](https://topology-tool-kit.github.io/doc/html/classttkDataSetToTable.html)

[DimensionReduction](https://topology-tool-kit.github.io/doc/html/classttkDimensionReduction.html)

[FlattenMultiBlock](https://topology-tool-kit.github.io/doc/html/classttkFlattenMultiBlock.html)

[GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html)

[MergeBockTables](https://topology-tool-kit.github.io/doc/html/classttkMergeBockTables.html)

[MergeTreePrincipalGeodesics](https://topology-tool-kit.github.io/doc/html/classttkMergeTreePrincipalGeodesics.html)

[MergeTreePrincipalGeodesicsDecoding](https://topology-tool-kit.github.io/doc/html/classttkMergeTreePrincipalGeodesicsDecoding.html)

[MergeTreeDistanceMatrix](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeDistanceMatrix.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[PointSetToSurface](https://topology-tool-kit.github.io/doc/html/classttkPointSetToSurface.html)

[ProjectionFromTable](https://topology-tool-kit.github.io/doc/html/classttkProjectionFromTable.html)

