# Merge Trees via ExTreeM

![Merge Tree via ExTreeM example Image](https://topology-tool-kit.github.io/img/gallery/mergeTreeExTreeM.jpg)


## Pipeline description
This example computes the merge tree and the join tree from an electronic density of the Adenine-Thymine molecular complex.

The ascending and descending segmentations needed for the computation are computed using [PathCompression](https://topology-tool-kit.github.io/doc/html/classttkPathCompression.html). They are computed by their own filter in this example, but generally, they will be computed by the [MergeTree](https://topology-tool-kit.github.io/doc/html/classttkMergeTree.html) if they don't exist already.

The python script simply computes the segmentation and saves the geometry of the join and split trees `.vtu` files.

## ParaView
To reproduce the example in Paraview, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/mergeTreeExTreeM.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/mergeTreeExTreeM.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/mergeTreeExTreeM.py
```


## Inputs
- [at.vti](https://github.com/topology-tool-kit/ttk-data/raw/dev/at.vti): A molecular dataset: a three-dimensional regular grid with 1 scalar field, the electronic density in the Adenine Thymine complex.

## Outputs
-  `joinTree.vtu`: the join tree.
-  `splitTree.vtu`: the split tree.


## C++/Python API

[PathCompression](https://topology-tool-kit.github.io/doc/html/classttkPathCompression.html)

[MergeTree](https://topology-tool-kit.github.io/doc/html/classttkMergeTree.html)
