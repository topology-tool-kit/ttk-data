# Molecular vibration on the prism hexamer

![Molecular Vibration on Prism Hexamer example Image]

## Pipeline description

This example computes the so-called *Bond Occurence Rate* from an ensemble of data-sets of electron density fields modeling a molecular system under a chemical perturbation. In this example, we visualize the *Molecular Vibration* of the *Prism Hexamer*. The datasets chosen in this example are extracted from (https://github.com/thom-dani/BondMatcher).

First, we select the files in database of electron density field with the filters [CinemaReader1](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html), [CinemaQuery](https://topology-tool-kit.github.io/doc/html/classttkCinemaQuery.html) and [CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html).

Second, we compute the opposite of the density and we normalize the resulting scalar field (in between 0 and 1) with the filter [ScalarFieldNormalizer](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldNormalizer.html) to facilitate the subsequent processing steps.

Third, we make a simplification with the filter [TopologicalSimplificationByPersistence](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplificationByPersistence.html) to remove the least significant extreama. We aim to obtain exactly 18 minima for each data-set corresponding to the 18 atoms of the molecular system.

The next step is to calculate the [MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html) of each scalar field. We use an algorithm to remove the least significant saddle connectors and we obtain the *Extremum Graph* of the molecular system in which each minima represent an atom and each *Unstable Set* (i.e 1_separatrices of type 0) represents a chemical interaction.

After we applied a Threshold on the 1_separatrices to only keep the *Unstable Set*, we apply the filter [SeparatrixStability] on to obtain the *Bond Occurence Rate* of each chemical interaction across the ensemble of data-sets.

Finally the geometry of the 1-separatrices are slightly smoothed with the filter [GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html) (`50` iterations each).

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

- [vibrationPrism.cdb](https://github.com/thom-dani/BondMatcher): Prism hexamer under molecular vibration, one equilibrium state an 20 perturbed states.

## Outputs

- `bondOccurenceRates.vtm`: Extremum graph of each state with the bond occurence rate on each 1_separatrices.

## C++/Python API


[CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html)

[CinemaQuery](https://topology-tool-kit.github.io/doc/html/classttkCinemaQuery.html)

[CinemaReader1](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html)

[GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html)

[MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html)

[SeparatrixStability]

[ScalarFieldNormalizer](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldNormalizer.html)

[TopologicalSimplificationByPersistence](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplificationByPersistence.html)
