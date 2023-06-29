# Morse persistence 
<iframe width="100%" height="420"
src="https://www.youtube.com/embed/xjKh6YTq5RA" frameborder="0"
allowfullscreen></iframe>

<!-- ![Morse Persistence example Image](https://topology-tool-kit.github.io/img/gallery/morsePersistence.jpg) -->

## Pipeline description

The first step is to create the data for our example. A plane is created to which we add random scalar values to create noise. The obtained scalar field is smoothed using the [ScalarFieldSmoother](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldSmoother.html). A sum of sine as scalar values is also added to create the nine main hills.

Then, the [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) is computed and thresholds are applied base on persistence to maintain only the most persistent features. This results in a simplified persistence diagram (bottom right view in the above screenshot).

The [PersistenceCurve](https://topology-tool-kit.github.io/doc/html/classttkPersistenceCurve.html) is also computed (top right view in the above screenshot).

The simplified persistence diagram is then used as a constraint for the [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html) of the input scalar data.

This simplified data is then used as the input of the computation of [MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html) (center view, above screenshot). This complex is composed of elements of 3 dimensions: dimension 0, which corresponds to the critical points of the Morse-Smale Complex, dimension 1, which corresponds to its edges (in grey in the screenshot) and dimension 2, which corresponds to its surfaces.

## ParaView
To reproduce the above screenshot, go to your `ttk-data`  directory and enter the following command:
``` bash
paraview states/morsePersistence.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/morsePersistence.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/morsePersistence.py
```


## Inputs
- None

## Outputs
- `PersistenceDiagram.vtu`: the output persistence diagram in VTK file format (bottom right view, above screenshot). You are free to change the `vtu` file extension to that of any other supported file format (e.g. `csv`) in the above python script.
- `PersistenceCurve.csv`: the output persistence curve.
- `MorseComplexeCriticalPoints.vtp`: the output critical points (or 0 dimensional elements) of the Morse Smale Complex in VTK file format (center view, above screenshot). You are free to change the `vtp` file extension to that of any other supported file format (e.g. `csv`) in the above python script.
- `MorseComplexe1Separatrices.vtp`: cylinders, representing the edges (or 1 dimensional elements) of the output Morse Smale Complexe in VTK file format (center view, above screenshot). You are free to change the `vtp` file extension to that of any other supported file format (e.g. `csv`) in the above python script.
- `MorseComplexeSegmentation.vtp`: surfaces, representing the segmentation  of the output Morse Smale Complexe in VTK file format (center view, above screenshot). You are free to change the `vtp` file extension to that of any other supported file format (e.g. `csv`) in the above python script.

## C++/Python API

[MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html)


[PersistenceCurve](https://topology-tool-kit.github.io/doc/html/classttkPersistenceCurve.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[ScalarFieldSmoother](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldSmoother.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)
