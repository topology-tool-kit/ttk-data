# Topological Autoencoders++ Teaser

![Topological Autoencoders++ Teaser screenshot](https://topology-tool-kit.github.io/img/gallery/topoAEppTeaser.jpg)

## Pipeline description
This example illustrates the [Topological Autoencoders++](https://arxiv.org/abs/2502.20215) dimensionality reduction technique on two toy examples and one real-world example. [Topolocial Autoencoders](https://proceedings.mlr.press/v119/moor20a.html) used autoencoders with a topological regularization term that constrains the preservation of the 0-dimensional persistent homology. Topological Autoencoders++ proposes a regularization term and efficient algorithms to additionally constrain the preservation of 1-dimensional persistent homology.

Three examples are provided as CSV ASCII files (one line per point, one column per dimension). These are two toy point clouds in 3D and one high-dimensional image dataset, which Topological Autoencoders++ projects down to 2D. Each of these point clouds features one or several significant 1-dimensional persistent homology class(es), that Topological Autoencoders++ aims to preserve when projecting down to 2D.

The dataset [twistedEllipse.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/twistedEllipse.csv) consists in an ellipse embedded in 3D which has been twisted along its long axis (top left view in the above screenshot). It features one significant persistent pair.

The dataset [K4.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/K4.csv) contains points noisily sampled next to the edges of a regular tetrahedron embedded in 3D. It features three significant persistent pairs. For each of them, a persistent generator is computed (one color per generator in the above screenshot, top center view). 

The dataset [coil20.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/coil20.csv) contains 20 object classes, each seen from 72 different angles. The subset of this dataset containing only the pictures of the first object (a rubber duck, data is shown in the top right table in the above screenshot) features one significant persistent pair, that corresponds to the fact these views from different angles live on a manifold homeomorphic to a circle.

For each of these datasets, Topological Autoencoders++ computes a 2D projection (corresponding bottom views in the above screenshot).

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/topoAEppTeaser.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/topoAEppTeaser.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/topoAEppTeaser.py
```


## Inputs
- [twistedEllipse.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/twistedEllipse.csv): a 3D point cloud in CSV ASCII format (one line per point, one column per dimension), which exhibits 1 significant persistent cycle.
- [K4.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/K4.csv): a 3D point cloud in CSV ASCII format (one line per point, one column per dimension), which exhibits 3 significant persistent cycles.
- [coil20.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/coil20.csv): a high-dimensional point cloud in CSV ASCII format (one line per point, one column per dimension), of which the first class of images exhibits 1 significant persistent cycle.

## Outputs
- `twistedEllipse_topoAE++.csv`: the output 2D projection of the [twistedEllipse.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/twistedEllipse.csv) dataset in CSV ASCII format (one line per point, one column per dimension).
- `K4_topoAE++.csv`: the output 2D projection of the [K4.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/K4.csv) dataset in CSV ASCII form
  at (one line per point, one column per dimension).
- `coil20-1_topoAE++csv`: the output 2D projection of the first class of the [coil20.csv](https://github.com/topology-tool-kit/ttk-data/raw/dev/coil20.csv) dataset in CSV ASCII form at (one line per point, one column per dimension).

## C++/Python API
[DimensionReduction](https://topology-tool-kit.github.io/doc/html/classttkDimensionReduction.html)
