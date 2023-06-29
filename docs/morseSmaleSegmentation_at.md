# Morse-Smale Segmentation AT

![MorseSmale Segmentation AT Example Image](https://topology-tool-kit.github.io/img/gallery/morseSmaleSegmentation_at.jpg)

## Pipeline description
This example computes the ascending and descending Morse segmentations from an electronic density of the Adenine-Thymine molecular complex.
The descending segmentation separators (red) represent the influence areas of maxima, giving each atom its own pocket since they are the most dense points in the dataset. The ascending segmentation separators (blue) represent the influence area of minima, providing the interactions (covalent and non-covalent) between the atoms in this example.

The segmentations are computed using [PathCompression](https://topology-tool-kit.github.io/doc/html/classttkPathCompression.html).
The separating geometry is generated using [MarchingTetrahedra](https://topology-tool-kit.github.io/doc/html/classttkMarchingTetrahedra.html)

The python script simply computes the segmentation and saves the separating
surfaces as `.vtu` files.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/morseSmaleSegmentation_at.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/morseSmaleSegmentation_at.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/morseSmaleSegmentation_at.py
```


## Inputs
- [at.vti](https://github.com/topology-tool-kit/ttk-data/raw/dev/at.vti): A molecular dataset: a three-dimensional regular grid with 1 scalar field, the electronic density in the Adenine Thymine complex.

## Outputs
-  `ascendingSeparatorAt.vtu`: the ascending separator geometry.
-  `descendingSeparatorAt.vtu`: the descending separator geometry.


## C++/Python API

[GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html)

[MarchingTetrahedra](https://topology-tool-kit.github.io/doc/html/classttkMarchingTetrahedra.html)

[PathCompression](https://topology-tool-kit.github.io/doc/html/classttkPathCompression.html)

