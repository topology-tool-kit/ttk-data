# Persistence Diagram Clustering 

![Persistence Diagram Clustering example Image](https://topology-tool-kit.github.io/img/gallery/persistenceDiagramClustering.jpg)

## Pipeline description
This example first loads an ensemble of scalar fields inside a cinema database from disk.
Then, the [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) is computed on each scalar field.

All these diagrams are passed to [PersistenceDiagramClustering](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagramClustering.html) to compute a clustering in the space of persistence diagrams.
The clustering is done using a *progressive* algorithm. In particular, a time constraint can be set to the approach. The algorithm delivers an partial but meaningful result within this constraint, prioritizing high-persistence
pairs in the computation.
Each centroid is also an explicit persistence diagram. Upon convergence, it is a Wasserstein barycenter of the diagrams within each cluster. As such, it is representative of the repartition of topological features within each cluster.

In the ParaView state, the extrema corresponding to each centroids are represented in the original 3d domain, scaled by topological persistence.

The python script computes the clustering and saves the related classification in a .csv file. Additionally, the resulting diagram centroids are saved as a multiblock dataset.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/persistenceDiagramClustering.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/persistenceDiagramClustering.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/persistenceDiagramClustering.py
```


## Inputs
- [Isabel.cdb](https://github.com/topology-tool-kit/ttk-data/tree/dev/Isabel.cdb): a cinema database containing 12 scalarfields defined on a regular grid, corresponding to 12 timesteps of a hurricane simulation.

## Outputs
-  `PersistenceDiagramClustering_clustering.csv`: the output classification.
-  `PersistenceDiagramClustering_centroids.vtm`: the output centroids.


## C++/Python API

[CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html)

[CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[PersistenceDiagramClustering](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagramClustering.html)
