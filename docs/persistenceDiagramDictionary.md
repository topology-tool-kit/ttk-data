# Persistence Diagram Dictionary

<!-- ![Merge Tree Temporal Reduction example Image](https://topology-tool-kit.github.io/img/gallery/mergeTreeTemporalReduction.jpg) -->

## Pipeline description
This example first loads an ensemble of scalar fields inside a cinema database from disk.
Then, the [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) is computed on each scalar field.

All these diagrams are passed to [PersistenceDiagramDictionary](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagramDictionary.html) to compute an ensemble of diagrams called dictionary and barycentric weights.
This dictionary and those weights will then be used to compute barycenters of persistence diagrams as approximations of the input diagrams by using [PersistenceDiagramDictionaryDecoding](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagramDictionaryDecoding.html).
The mentionned barycenters are computed using the algorithm implemented in [PersistenceDiagramClustering](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagramClustering.html).

The algorithm uses a classical gradient descent to optimize both outputs, it can also use a *progressive* approach to further facilitate the optimization.

In the ParaView state, we have a visual comparison between three input diagrams and their respective approximation. Furthermore we also have a planar visualization of computed barycenters and the dictionary.

The python script computes the dictionary and the barycentric weights, it then saves the dictionary in a multiblock dataset and the weights in a .csv file.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/persistenceDiagramDictionary.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/persistenceDiagramDictionary.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/persistenceDiagramDictionary.py
```


## Inputs
- [Isabel.cdb](https://github.com/topology-tool-kit/ttk-data/tree/dev/Isabel.cdb): a cinema database containing 12 regular grids.

## Outputs
-  `PD-Dictionary_dict.vtm`: the output dictionary.
-  `PD-Dictionary_weights.csv`: the output weights.


## C++/Python API
[CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html)

[CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[PersistenceDiagramClustering](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagramClustering.html)

[PersistenceDiagramDictionary](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagramDictionary.html)

[PersistenceDiagramDictionaryDecoding](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagramDictionaryDecoding.html)

