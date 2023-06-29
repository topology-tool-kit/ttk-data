# Karhunen-Love Digits 64-Dimensions 

![Karhunen-Love Digits 64-Dimensions screenshot](https://topology-tool-kit.github.io/img/gallery/karhunenLoveDigits64Dimensions.jpg)

## Pipeline description
This example performs a persistence driven clustering of a high-dimensional data set, specifically a [collection of 2000 images representing hand written digits](https://archive.ics.uci.edu/ml/datasets/Multiple+Features). Each image is encoded by its Karhunen-Love coefficients, a 64-dimensional vector. This results in a point cloud of 2000 points (2000 rows), living in 64 dimensions (64 columns).

The ground truth classification for each point is provided by the column `Field0` (point color in the bottom right view, above screenshot), which indicates the digit represented by the corresponding image.

The pipeline starts by using [DimensionReduction](https://topology-tool-kit.github.io/doc/html/classttkDimensionReduction.html) (with tSNE) to project the data down to 2D.

Next, the density of the projected 2D point cloud is estimated with a Gaussian kernel, by the `GaussianResampling`  filter, coupled with the `Slice` filter (to restrict the estimation to a 2D plane). 

Next, the [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) of the density field is computed and only the 10 most persistent density maxima are selected (corresponding to the 10 classes, one per digit, bottom left view in the above screenshot).

Next, the simplified persistence diagram is used as a constraint for the [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html) of the density field.
The simplified density field then contains only 10 maxima and it is used as an input to the [Morse-Smale complex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html) computation, for the separation of the 2D space into the output clusters (background color in the bottom right view, above screenshot). 

Finally, the cluster identifier of each input point is given by the identifier of the 
corresponding ascending manifold of the Morse-Smale complex (`AscendingManifold`), with the `ResampleWithDataset` filter.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/karhunenLoveDigits64Dimensions.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/karhunenLoveDigits64Dimensions.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/karhunenLoveDigits64Dimensions.py
```


## Inputs
- [karhunenLoveDigits64Dimensions.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/karhunenLoveDigits64Dimensions.csv): an input high dimensional point cloud (2000 points in 64 dimensions).

## Outputs
- `OutputClustering.csv`: the output clustering of the input point cloud (output cluster identifier: `AscendingManifold` column, ground truth: `Field0`)

## C++/Python API
[DimensionReduction](https://topology-tool-kit.github.io/doc/html/classttkDimensionReduction.html)

[IdentifierRandomizer](https://topology-tool-kit.github.io/doc/html/classttkIdentifierRandomizer.html)

[Morse-Smale complex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)
