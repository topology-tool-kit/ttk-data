# Manifold Check

![Manifold check screenshot](https://topology-tool-kit.github.io/img/gallery/manifoldCheck.jpg)

## Pipeline description

This example loads three different hexahedral geometry files from disk.
In a pre-processing, each geometry is tetrahedralized, which is used as input data.

On each of the three geometries, [ManifoldCheck](https://topology-tool-kit.github.io/doc/html/classttkManifoldCheck.html) is executed. This filters adds link numbers to vertices and cells, which can be used to detect and extract non-manifold vertices (left), edges (middle), and faces (right).

## ParaView

To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/manifoldChecks.pvsm
```

## Python code

### Non-manifold Vertices

``` python  linenums="1"
--8<-- "python/manifoldCheck0.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/manifoldCheck0.py
```


### Non-manifold Edges

``` python  linenums="1"
--8<-- "python/manifoldCheck1.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/manifoldCheck1.py
```


### Non-manifold Faces

``` python  linenums="1"
--8<-- "python/manifoldCheck2.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/manifoldCheck2.py
```


## Inputs

- [manifoldCheck0.vtu](https://github.com/topology-tool-kit/ttk-data/raw/dev/manifoldCheck0.vtu): example mesh with non-manifold vertices
- [manifoldCheck1.vtu](https://github.com/topology-tool-kit/ttk-data/raw/dev/manifoldCheck1.vtu): example mesh with non-manifold edges
- [manifoldCheck2.vtu](https://github.com/topology-tool-kit/ttk-data/raw/dev/manifoldCheck2.vtu): example mesh with non-manifold faces


## Outputs

- `manifoldCheck0_check.vtu`, `manifoldCheck1_check.vtu`, `manifoldCheck2_check.vtu`: tetrhedralized geometry with link numbers
- `manifoldCheck0_non_manifold.vtu`: non-manifold vertices in `manifoldCheck0.vtu`
- `manifoldCheck1_non_manifold.vtu`: non-manifold edges in `manifoldCheck1.vtu`
- `manifoldCheck2_non_manifold.vtu`: non-manifold faces in `manifoldCheck2.vtu`

## C++/Python API

[ManifoldCheck](https://topology-tool-kit.github.io/doc/html/classttkManifoldCheck.html) 
