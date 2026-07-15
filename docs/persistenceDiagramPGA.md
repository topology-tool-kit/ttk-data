# Persistence Diagram Principal Geodesic Analysis 

![Persistence Diagram Principal Geodesic Analysis example Image](https://topology-tool-kit.github.io/img/gallery/persistenceDiagramPGA.jpg)

## Pipeline description
This example first loads an ensemble of scalar fields within a cinema database from disk.
Then, the [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) is computed on each scalar field.

All these diagrams are passed to [MergeTreePrincipalGeodesics](https://topology-tool-kit.github.io/doc/html/classttkMergeTreePrincipalGeodesics.html) to compute Principal Geodesic Analysis (PGA) in the metric space of persistence diagrams. 

Then the filter [MergeTreePrincipalGeodesicsDecoding](https://topology-tool-kit.github.io/doc/html/classttkMergeTreePrincipalGeodesics.html) is used to reconstruct the input diagrams, to sample evenly diagrams along the principal geodesics and to sample a discrete grid of persistence diagrams of the PGA basis. 

A distance matrix is then computed with [MergeTreeDistanceMatrix](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeDistanceMatrix.html) with the diagrams of the grid. This distance matrix is used as input of [DimensionReduction](https://topology-tool-kit.github.io/doc/html/classttkDimensionReduction.html) to compute a MultiDimensional Scaling (MDS), performing a dimensionality reduction in 3D, thus representing the Wasserstein metric space as a curved surface (top right view, using the [PointSetToSurface](https://topology-tool-kit.github.io/doc/html/classttkPointSetToGrid.html) module). A planar representation of the ensemble is also available (bottom, using the [ProjectionFromTable](https://topology-tool-kit.github.io/doc/html/classttkProjectionFromTable.html) module from the PGA coefficients).

In terms of visualisation, a scalar field of each cluster is displayed. The original diagrams are displayed alongside their reconstruction on their right. The persistence pairs of the diagrams are colored by ID to see what features they correspond to in the scalar field.

The 3D and 2D surfaces are displayed with the persistence correlation view on the right. The 12 scalar fields are colored by Cluster ID. 

The python script computes the PD-PGA and saves the resulting coefficients of the input diagrams.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview --state=states/persistenceDiagramPGA.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/persistenceDiagramPGA.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/persistenceDiagramPGA.py
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

[IcospheresFromPoints](https://topology-tool-kit.github.io/doc/html/classttkIcospheresFromPoints.html)

[IdentifyByScalarField](https://topology-tool-kit.github.io/doc/html/classttkIdentifyByScalarField.html)

[MergeBockTables](https://topology-tool-kit.github.io/doc/html/classttkMergeBockTables.html)

[MergeTreeDistanceMatrix](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeDistanceMatrix.html)

[MergeTreePrincipalGeodesics](https://topology-tool-kit.github.io/doc/html/classttkMergeTreePrincipalGeodesics.html)

[MergeTreePrincipalGeodesicsDecoding](https://topology-tool-kit.github.io/doc/html/classttkMergeTreePrincipalGeodesicsDecoding.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[PointSetToCurve](https://topology-tool-kit.github.io/doc/html/classttkPointSetToCurve.html)

[PointSetToSurface](https://topology-tool-kit.github.io/doc/html/classttkPointSetToSurface.html)

[ProjectionFromTable](https://topology-tool-kit.github.io/doc/html/classttkProjectionFromTable.html)

