# Persistent Generators Household Analysis

<iframe width="100%" height="420"
src="https://www.youtube.com/embed/mCPoIjG2URo" frameborder="0"
allowfullscreen></iframe>


## Pipeline description

This example shows the detection of a circular pattern in high-dimensional data.
The data contains seven mesurements of electric power consumption for a single household over two years, for a daily sampling.
This can be interpreted as 700 points (on per day) in R^7.

The distance matrix between these points is computed using [TableDistanceMatrix](https://topology-tool-kit.github.io/doc/html/classttkTableDistanceMatrix.html).
Using the distance matrix, a clustering of the input data is performed using ParaView's K-means algorithm (with k=8).
The points are then embedded in 3D using MDS, with [DimensionReduction](https://topology-tool-kit.github.io/doc/html/classttkDimensionReduction.html).

At this point, the 2-dimensional Rips complex is computed with [RipsComplex](https://topology-tool-kit.github.io/doc/html/classttkRipsComplex.html) from the high-dimensional point cloud, and shown in 3D via MDS projection.

Finally an infinitely persistent 1-cycle is extracted from the Rips complex with [PersistentGenerators](https://topology-tool-kit.github.io/doc/html/classttkPersistentGenerators.html), on the *diameter* function.
This cycle captures a circular pattern present in the data, implying that in
practice, continuous displacements from one cluster to another are
likely to imply transformations through other clusters present along the cycle.

The python script saves the resulting point cloud, Rips complex and output cycle as vtk files.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/persistentGenerators_householdAnalysis.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/persistentGenerators_householdAnalysis.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/persistentGenerators_householdAnalysis.py
```


## Inputs
- [household_part1_ID_daily.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/household_part1_ID_daily.csv): A csv file containing the high-dimensional data.

## Outputs
-  `PersistentGeneratorsHouseholdAnalysis_points.vtp`: the high-dimensionnal point cloud embedded in 3D.
-  `PersistentGeneratorsHouseholdAnalysis_ripsComplex`: the 2-dimensional Rips complex of the point cloud.
-  `PersistentGeneratorsHouseholdAnalysis_cycle`: the infinitely persistent 1-cycle of the Rips complex.

## C++/Python API

[DimensionReduction](https://topology-tool-kit.github.io/doc/html/classttkDimensionReduction.html)

[PersistentGenerators](https://topology-tool-kit.github.io/doc/html/classttkPersistentGenerators.html)

[RipsComplex](https://topology-tool-kit.github.io/doc/html/classttkRipsComplex.html)

[TableDistanceMatrix](https://topology-tool-kit.github.io/doc/html/classttkTableDistanceMatrix.html)

