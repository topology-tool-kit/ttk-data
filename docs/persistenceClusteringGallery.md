# Persistence Clustering Gallery

![Persistence Clustering Gallery Image](https://topology-tool-kit.github.io/img/gallery/persistenceClusteringGallery.jpeg)

The Persistence Clustering Gallery is composed of the following examples (from left to right):

- [Persistence clustering0](../persistenceClustering0/)
- [Persistence clustering1](../persistenceClustering1/)
- [Persistence clustering2](../persistenceClustering2/)
- [Persistence clustering3](../persistenceClustering3/)
- [Persistence clustering4](../persistenceClustering4/)

Each example is explained in more details in its own documentation and is shown in the above screenshot in a pair of images, one showing the dataset (upper half), the other showing the results of the pipeline (bottom half).

## Pipeline description

All examples of the Gallery have a similar pipeline. 

First, it loads a point cloud from disk, then it computes a mesh on which a density field is obtained with a Gaussian Resampling on the points (top view in the above screenshot). This density field will be considered as the input scalar data.

Next, a [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) is computed and thresholds are applied base on persistence to maintain only the features with a persistence above a certain value. The result is a simplified persistence diagram.

The simplified persistence diagram is then used as a constraint for the [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html) of the input scalar data, giving us a simplified data.

From there a [MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html) is computed (bottom view in the above screenshot) then smoothed. Finally, by using the identifier of the 2-dimension cell of the Morse Smale complex where one point lands, a cluster is given to it.

## ParaView
To reproduce the above screenshot, go to your `ttk-data`  directory and enter the following command:
``` bash
paraview states/persistenceClusteringGallery.pvsm
```

## Python code

### Persistence clusering 0

``` python  linenums="1"
--8<-- "python/persistenceClustering0.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/persistenceClustering0.py
```


### Persistence clusering 1

``` python  linenums="1"
--8<-- "python/persistenceClustering1.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/persistenceClustering1.py
```


### Persistence clusering 2

``` python  linenums="1"
--8<-- "python/persistenceClustering2.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/persistenceClustering2.py
```


### Persistence clusering 3

``` python  linenums="1"
--8<-- "python/persistenceClustering3.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/persistenceClustering3.py
```


### Persistence clusering 4


``` python  linenums="1"
--8<-- "python/persistenceClustering4.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/persistenceClustering4.py
```



## C++/Python API

[GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)

[MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html)
