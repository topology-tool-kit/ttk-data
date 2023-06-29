# Persistence Clustering 0

![Persistence Clustering 0 screenshot](https://topology-tool-kit.github.io/img/gallery/persistenceClustering0.jpeg)

## Pipeline description
This example performs a persistence driven clustering of a 2D toy data set, taken from the [scikit-learn examples](https://scikit-learn.org/stable/modules/clustering.html).
Please check out the [Karhunen-Love Digits 64-Dimensions example](../karhunenLoveDigits64Dimensions/) for an application of this pipeline to a real-life, high-dimensional, data set.

The pipeline starts by estimating the density of the input point cloud with a Gaussian kernel, by the `GaussianResampling`  filter, coupled with the `Slice` filter (to restrict the estimation to a 2D plane).

Next, the [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) of the density field is computed and only the 2 most persistent density maxima are selected (corresponding to the desired 2 output clusters, bottom left view in the above screenshot).

Next, the simplified persistence diagram is used as a constraint for the [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html) of the density field (top right view, above screenshot).
The simplified density field then contains only 2 maxima and it is used as an input to the [Morse-Smale complex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html) computation, for the separation of the 2D space into the output clusters (background color in the bottom right view, above screenshot).

Finally, the cluster identifier of each input point is given by the identifier of the 
corresponding ascending manifold of the Morse-Smale complex (`AscendingManifold`), with the `ResampleWithDataset` filter.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/persistenceClustering0.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/persistenceClustering0.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/persistenceClustering0.py
```


## Inputs
- [clustering0.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/karhunenLoveDigits64Dimensions.csv): a 2D point cloud taken from the [scikit-learn examples](https://scikit-learn.org/stable/modules/clustering.html).

## Outputs
- `OutputClustering.csv`: the output clustering of the input point cloud (output cluster identifier: `AscendingManifold` column)

## C++/Python API
[Morse-Smale complex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)
