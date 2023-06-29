# Tectonic Puzzle 

![Tectonic Puzzle example
Image](https://topology-tool-kit.github.io/img/gallery/geology.jpg)

## Pipeline description

This example processes a two-dimensional geophysics model of the Earth
surface to segment it according to the tectonic plates.

The outer surface of the data-set is first extracted with a
combination of ParaView's `Connectivity` and `Threshold`. Then, the
`log10` of the `Viscosity` scalar field is computed with a
`Calculator` (bottom-right view on the above screenshot).

Several passes of topological simplification are then combined, using
[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html),
[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)
and
[MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html)
to further clean the scalar field. The Persistence Diagram of the
scalar field at the end of this cleaning step is represented in the
bottom-right view on the above screenshot.

Once this is done, since the low values of the scalar field represent the
plates borders and the regions of high values the plates themselves,
the `Descending 1-Separatrices` of the Morse-Smale Complex follow the
plates borders and the `AscendingManifold` Segmentation of the
Morse-Smale Complex gives us the expected segmentation of the tectonic
plates (top-right view on the above screenshot).

Finally, the
[IdentifierRandomizer](https://topology-tool-kit.github.io/doc/html/classttkIdentifierRandomizer.html)
filter is used to color neighbor cells with a distinct color (top
right view on the above screenshot).



## ParaView

To reproduce the above screenshot, go to your
[ttk-data](https://github.com/topology-tool-kit/ttk-data) directory
and enter the following command:

``` bash
paraview states/tectonicPuzzle.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/tectonicPuzzle.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/tectonicPuzzle.py
```


## Inputs

- [tectonicPuzzle.vtu](https://github.com/topology-tool-kit/ttk-data/raw/dev/tectonicPuzzle.vtu):
  two 2-dimensional spheres (one around the other) made up of a
  triangular mesh. There are several point data arrays attached to it.
  Those scalar fields represent geophysics measures on the earth
  surface (and at a certain depth under it); only the `Viscosity`
  field will be used in the current example.

## Outputs

- `Segmentation.vtu`: the output segmentation in VTK file format (top
  right view, above screenshot). This corresponds to a segmentation of
  the tectonic plates from the `Viscosity` scalar field.


## C++/Python API
[IcospheresFromPoints](https://topology-tool-kit.github.io/doc/html/classttkIcospheresFromPoints.html)

[IdentifierRandomizer](https://topology-tool-kit.github.io/doc/html/classttkIdentifierRandomizer.html)

[MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)



