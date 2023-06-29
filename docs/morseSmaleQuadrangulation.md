# Morse-Smale Quadrangulation

<!--[![Morse-Smale Quadrangulation example video tutorial](https://topology-tool-kit.github.io/img/gallery/morseSmaleQuadrangulation.jpg)](https://www.youtube.com/watch?v=eNW8l5PlgpU)-->

<iframe width="100%" height="420"
src="https://www.youtube.com/embed/eNW8l5PlgpU" frameborder="0"
allowfullscreen></iframe>

## Pipeline description

This example first loads a mecanical model as a 2D triangle mesh from
disk. This mechanical model embeds a collection of scalar fields that
corresponds to the output of the
[EigenField](https://topology-tool-kit.github.io/doc/html/classttkEigenField.html)
module. This module generated a family of functions that are coupled
to the form of the dataset (basically, they are eigenfunctions of the
laplacian matrix of the triangulation, sorted by decreasing eigenvalue
magnitude).

In a pre-processing step, the 83rd EigenFunction is extracted and
normalized with
[ScalarFieldNormalizer](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldNormalizer.html)
then simplified using
[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)
and
[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html).

We then compute the
[MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html)
of the simplified scalar field. The critical points are evenly spread
onto the 2D surface and the 1-separatrices will form the base of the
quadrangulation (left view on the above screenshot).

The filter
[MorseSmaleQuadrangulation](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleQuadrangulation.html)
creates a coarse quadrangulation of the input mesh using the
Morse-Smale complex critical points and 1-separatrices.

This coarse quadrangulation is eventually refined with the
[QuadrangulationSubdivision](https://topology-tool-kit.github.io/doc/html/classttkQuadrangulationSubdivision.html)
filter (right view on the above screenshot).

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/morseSmaleQuadrangulation.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/morseSmaleQuadrangulation.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/morseSmaleQuadrangulation.py
```


## Inputs
- [rockerArm.vtu](https://github.com/topology-tool-kit/ttk-data/raw/dev/rockerArm.vtu): a two-dimensional triangulated mechanical model.

## Outputs
- `Quadrangulation.vtp`: the output quadrangulated surface.


## C++/Python API

[EigenField](https://topology-tool-kit.github.io/doc/html/classttkEigenField.html)

[MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html)

[MorseSmaleQuadrangulation](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleQuadrangulation.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[QuadrangulationSubdivision](https://topology-tool-kit.github.io/doc/html/classttkQuadrangulationSubdivision.html)

[ScalarFieldNormalizer](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldNormalizer.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)

