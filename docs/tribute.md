# Tribute to Edelsbrunner and Harer's book

![Tribute screenshot](https://topology-tool-kit.github.io/img/gallery/tribute.jpg)

## Pipeline description

This example loads a PNG image from disk, from which a triangle mesh with gray-scale scalar values is created.

Then, the [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) is computed and thresholds are applied base on persistence to maintain only the most persistent features. This results in a simplified persistence diagram (top right; non-simplified persistence diagram shown in gray).

The simplified persistence diagram is then used as a constraint for the [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html) of the input scalar data.

This simplified data is then used as the input of the computation of the [MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html). Its ascending manifolds, separatrices and critical points are shown in the bottom views (with scalar value mapped to height in the bottom right view). The separatrices are also shown, as overlay over the original scalar data, in the top left view.

## ParaView

To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
$ paraview states/tribute.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/tribute.py"
```

## Inputs

- [tribute.png](https://github.com/topology-tool-kit/ttk-data/raw/dev/tribute.png): PNG image of a microscopy of cell sheet morphogenesis (from Edelsbrunner & Harer's book, page 217)

## Outputs

- `triubute_segmentation.vtu`: segmentation of `tribute.png` into cells (Morse&ndash;Smale complex; data array `AscendingManifold`)

## C++/Python API

[IcospheresFromPoints](https://topology-tool-kit.github.io/doc/html/classttkIcospheresFromPoints.html) 

[IdentifierRandomizer](https://topology-tool-kit.github.io/doc/html/classttkIdentifierRandomizer.html) 

[MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html) 

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) 

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html) 
