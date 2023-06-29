# Persistent Generators Periodic Picture

![Persistent Generators Periodic Picture example Image](https://topology-tool-kit.github.io/img/gallery/persistentGenerators_periodicPicture.jpg)

## Pipeline description

This example shows the detection of a circular pattern in high-dimensional data.
100 greyscale pictures of resolution 32x32 of a syntethic terrain were taken in ParaView, from 100 viewpoints arranged along a circle, and stored in a cinema database.

The ParaView example starts by loading the database. The set of pictures and the corresponding viewpoints can be navigated using the time controls of ParaView.

This set of images can be interpreted as 100 points in R^1024. 
The distance matrix between these points is computed using [TableDistanceMatrix](https://topology-tool-kit.github.io/doc/html/classttkTableDistanceMatrix.html).
These points are then embedded in 3D using MDS, with [DimensionReduction](https://topology-tool-kit.github.io/doc/html/classttkDimensionReduction.html).

At this point, the 2-dimensional Rips complex is computed with [RipsComplex](https://topology-tool-kit.github.io/doc/html/classttkRipsComplex.html) from the high-dimensional point cloud, and shown in 3D via MDS projection.

Finally the infinitely persistent 1-cycle is extracted from the Rips complex with [PersistentGenerators](https://topology-tool-kit.github.io/doc/html/classttkPersistentGenerators.html), on the *diameter* function.
This cycle captures the circular pattern synthetically injected in the data.

The python script saves the resulting point cloud, Rips complex and output cycle as vtk files.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/persistentGenerators_periodicPicture.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/persistentGenerators_periodicPicture.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/persistentGenerators_periodicPicture.py
```


## Inputs
- [periodicPicture.cdb](https://github.com/topology-tool-kit/ttk-data/raw/dev/periodicPicture.cdb): A cinema database containing all 100 pictures, with metadata (the associated camera angle).

## Outputs
-  `PersistentGeneratorsPeriodicPicture_points.vtp`: the high-dimensionnal point cloud embedded in 3D.
-  `PersistentGeneratorsPeriodicPicture_ripsComplex.vtu`: the 2-dimensional Rips complex of the point cloud.
-  `PersistentGeneratorsPeriodicPicture_cycle.vtp`: the infinitely persistent 1-cycle of the Rips complex.


## C++/Python API

[CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html)

[CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html)

[DataSetToTable](https://topology-tool-kit.github.io/doc/html/classttkDataSetToTable.html)

[DimensionReduction](https://topology-tool-kit.github.io/doc/html/classttkDimensionReduction.html)

[MergeBlockTables](https://topology-tool-kit.github.io/doc/html/classttkMergeBlockTables.html)

[PersistentGenerators](https://topology-tool-kit.github.io/doc/html/classttkPersistentGenerators.html)

[RipsComplex](https://topology-tool-kit.github.io/doc/html/classttkRipsComplex.html)

[TableDistanceMatrix](https://topology-tool-kit.github.io/doc/html/classttkTableDistanceMatrix.html)

