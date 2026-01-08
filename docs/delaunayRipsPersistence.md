# Delaunay-Rips persistence

![Delaunay-Rips persistence screenshot](https://topology-tool-kit.github.io/img/gallery/delaunayRipsPersistence.jpg)

## Pipeline description
This example illustrates the use of the ``TTKDelaunayRipsPersistenceDiagram`` and ``TTKDelaunayRipsPersistenceGenerators`` filters to compute persistence diagrams (and associated persistent generators) of the Delaunay-Rips filtration of an input point set.

Three examples are provided. The first two are point sets in 3D (hence, with easily visualizable persistence generators) and the last is a point set in 5D given as a CSV ASCII file (one line per point, one column per dimension).

The dataset [67P-Churyumov-Gerasimenko.vtp](https://github.com/topology-tool-kit/ttk-data/raw/dev/67P-Churyumov-Gerasimenko.vtp) consists of a 3D mesh that is a scan of Comet 67P/Churyumov–Gerasimenko, as captured by the Rosetta mission. As this comet is a [contact binary](https://en.wikipedia.org/wiki/Contact_binary_(small_Solar_System_body)), the point set features two significant 2-dimensional persistent pairs (one very persistent, corresponding to the cavity enclosed by the surface, the other less persistent, corresponding to one of the lobes). A generator for each of them is shown (one color per generator in the above screenshot, top left view)

The dataset [K4.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/K4.csv) contains points noisily sampled next to the edges of a regular tetrahedron embedded in 3D. It features three significant 1-dimensional persistent pairs (cyan bars in the diagram). For each of them, a persistent generator is shown (one color per generator in the above screenshot, top center view).

The dataset [hypersphere5.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/coil20.csv) contains 10,000 points in 5D sampled next to a 4-sphere (some Gaussian noise is applied). This point set features one significant 4-dimensional persistent pair (red bar in the diagram).

For each of these datasets, its persistence diagrams are shown in the corresponding bottom views in the above screenshot.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/delaunayRipsPersistence.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/delaunayRipsPersistence.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/delaunayRipsPersistence.py
```

## Inputs
- [67P-Churyumov-Gerasimenko.vtp](https://github.com/topology-tool-kit/ttk-data/raw/dev/67P-Churyumov-Gerasimenko.vtp): a 3D mesh in ``.vtp`` format.
- [K4.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/K4.csv): a 3D point set in CSV ASCII format (one line per point, one column per dimension).
- [hypersphere5.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/coil20.csv): a 5D point set in CSV ASCII format (one line per point, one column per dimension).

## Outputs
- `67PChuryumovGerasimenko_generator.csv`: a generator associated with the most persistent 2-dimensional persistent pair of the [67P-Churyumov-Gerasimenko.vtp](https://github.com/topology-tool-kit/ttk-data/raw/dev/67P-Churyumov-Gerasimenko.vtp) dataset in OBJ format.
- `67PChuryumovGerasimenko_diagram.csv`: the persistence diagrams of the [67P-Churyumov-Gerasimenko.vtp](https://github.com/topology-tool-kit/ttk-data/raw/dev/67P-Churyumov-Gerasimenko.vtp) dataset in CSV ASCII format.
- `K4_diagram.csv`: the persistence diagrams of the [K4.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/K4.csv) dataset in CSV ASCII format.
- `hypersphere5D_diagram.csv`: the persistence diagrams of the [hypersphere5.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/coil20.csv) dataset in CSV ASCII format.

## C++/Python API
[DelaunayRipsPersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkDelaunayRipsPersistenceDiagram.html)

[DelaunayRipsPersistenceGenerators](https://topology-tool-kit.github.io/doc/html/classttkDelaunayRipsPersistenceGenerators.html)
