# Persistence Diagram Dictionary

 ![Persistence Diagram Dictionary example Image](https://topology-tool-kit.github.io/img/gallery/persistenceDiagramDictionary.jpg) 

## Pipeline description

This example describes the usage of the dictionary of persistence diagrams for the topological analysis of ensemble data.

First, an ensemble of scalar fields is loaded from a cinema database.

Then, the [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) is computed for each scalar field.

All these diagrams are passed to [PersistenceDiagramDictionary](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagramDictionary.html) to compute:

1. an ensemble of atom diagrams called *dictionary*,
2. a set of barycentric weights (for each diagram), which can be interpreted as coordinates in the above dictionary.

This dictionary and those weights will then be used to compute barycenters of persistence diagrams as approximations of the input diagrams by using [PersistenceDiagramDictionaryDecoding](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagramDictionaryDecoding.html).
The mentioned barycenters are computed using the algorithm implemented in [PersistenceDiagramClustering](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagramClustering.html).

The algorithm uses a classical gradient descent to optimize both outputs. It can also use a *progressive* approach to further facilitate the optimization.

The above screenshot presents a visual comparison between three input diagrams (center, left) and their respective approximations (center, right). Furthermore, we also have a planar visualization of the computed barycenters (colored spheres) and the dictionary (atoms are represented with black spheres).

The python script below computes the dictionary and the barycentric weights. Then, it saves the dictionary in a multiblock dataset and the weights in a `.csv` file.

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
- [Isabel.cdb](https://github.com/topology-tool-kit/ttk-data/tree/dev/Isabel.cdb): a cinema database containing 12 volumetric scalar fields (defined on regular grids).

## Outputs
-  `PD-Dictionary_dict.vtm`: the output dictionary (i.e., set of atom diagrams).
-  `PD-Dictionary_weights.csv`: the output weights (the coordinate of the input ensemble in the dictionary).


## C++/Python API
[CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html)

[CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[PersistenceDiagramClustering](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagramClustering.html)

[PersistenceDiagramDictionary](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagramDictionary.html)

[PersistenceDiagramDictionaryDecoding](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagramDictionaryDecoding.html)

