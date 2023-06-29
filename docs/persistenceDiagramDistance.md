# Persistence Diagram Distance 

![Persistence Diagram Distance example Image](https://topology-tool-kit.github.io/img/gallery/persistenceDiagramDistance.jpg)

## Pipeline description
This example first loads an ensemble of twelve scalar fields inside a cinema database from disk. Two scalar fields are extracted from the ensemble.
Then, the [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) is computed on both fields.

[PersistenceDiagramClustering](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagramClustering.html) is then used to compute the Wasserstein distance between the two persistence diagrams.
The assignment problem associated to the distance is computed using the Auction algorithm, and the corresponding matchings are displayed in ParaView.
The actual distance is available in the field data of the 'matchings' output.

The python script computes the distance and prints it in the terminal output. Additionally, it saves the distance as a .csv file.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/persistenceDiagramDistance.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/persistenceDiagramDistance.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/persistenceDiagramDistance.py
```


## Inputs
- [Isabel.cdb](https://github.com/topology-tool-kit/ttk-data/tree/dev/Isabel.cdb): a cinema database containing 12 scalarfields defined on a regular grid, corresponding to 12 timesteps of a hurricane simulation.

## Outputs
-  `WassersteinDistance.csv`: the output distance between the two persistence diagrams.


## C++/Python API

[CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html)

[CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[PersistenceDiagramClustering](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagramClustering.html)
