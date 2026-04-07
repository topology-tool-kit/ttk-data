# Molecular Vibration

![Molecular Vibration on Prism Hexamer example Image](https://topology-tool-kit.github.io/img/gallery/molecularVibration.jpg)

## Pipeline description

This example computes the *Bond Occurrence Rate* from an ensemble of electron density fields modeling a molecular system (the so-called *Prism* water hexamer) under molecular vibration. 
Specifically, this example partly reproduces the Figure 7 of the paper [BondMatcher: H-Bond Stability Analysis in Molecular Systems](https://arxiv.org/abs/2504.03205).

The pipeline includes the following steps.

First, the appropriate datasets are read from disk using the filters [CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html), [CinemaQuery](https://topology-tool-kit.github.io/doc/html/classttkCinemaQuery.html), and [CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html). Specifically, the dataset `GeomID=10` (top right) corresponds to the equilibrium state of the molecule, while the datasets `GeomID=0` (bottom left) and `GeomID=20` (top left) correspond to its most extreme vibrations.

Second, for convenience, the opposite of the density is considered and normalized with the [ScalarFieldNormalizer](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldNormalizer.html) to facilitate the subsequent processing steps.

Third, [TopologicalSimplificationByPersistence](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplificationByPersistence.html) is used to remove spurious extrema from the data, such that only 18 minima remains for each dataset (for the 18 atoms of the water hexamers).

Next, for each scalar field, the [MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html) is computed. This complex is post-processed to cancel the least salient saddle-saddle pairs (see the checkbox `Return Saddle Connectors`). 
At this stage, the 1-dimensional separatrices of the complex are filtered, to only keep the saddle-minimum separatrices. This yields an *Extremum Graph*, which includes the minima of the scalar field and which connects them according to the saddle-minimum separatrices (representing chemical interactions, e.g., an H-bond or a covalent bond).

Finally, the *Bond Occurrence Rate* is computed from this extremum graph with the filter [SeparatrixStability](https://topology-tool-kit.github.io/doc/html/classttkSeparatrixStability.html) and it is visualized for the equilibrium state (bottom right). For each chemical interactionn, this quantity documents the rate of its occurrence in the ensemble (see the publication [BondMatcher: H-Bond Stability Analysis in Molecular Systems](https://arxiv.org/abs/2504.03205) for the formalization of this measure). Specifically, each occurrence rate is saved as the `CellDataArray` named `Occurrence`, itself associated to the output extremum graphs.

## ParaView

To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/molecularVibration.pvsm
```

## Python code

``` python  linenums="1"

--8<-- "python/molecularVibration.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/molecularVibration.py
```


## Inputs

- [molecularVibration.cdb](https://github.com/topology-tool-kit/ttk-data/molecularVibration.cdb/): Prism hexamer under molecular vibration, one equilibrium state and 2 perturbed states.

## Outputs

- `bondOccurenceRates.vtm`: Extremum graph of each state with its bond occurrence rate on each 1-dimensional separatrix.

## C++/Python API


[CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html)

[CinemaQuery](https://topology-tool-kit.github.io/doc/html/classttkCinemaQuery.html)

[CinemaReader1](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html)

[GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html)

[IdentifierRandomizer](https://topology-tool-kit.github.io/doc/html/classttkIdentifierRandomizer.html)

[MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html)

[SeparatrixStability](https://topology-tool-kit.github.io/doc/html/classttkSeparatrixStability.html)

[ScalarFieldNormalizer](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldNormalizer.html)

[TopologicalSimplificationByPersistence](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplificationByPersistence.html)
