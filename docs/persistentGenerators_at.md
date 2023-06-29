# Persistent Generators AT

![Persistent Generators AT example Image](https://topology-tool-kit.github.io/img/gallery/persistentGenerators_at.jpg)

## Pipeline description
This example computes the persistent one-dimensional generators of the electronic density of the Adenine-Thymine molecular complex.
These generators characterize the cycles in the interactions between atoms, whether they are covalent (cycles in the carbonate chains), or weaker non-covalent interactions (cycles in the hydrogen bonds).

Generators are computed using [PersistentGenerators](https://topology-tool-kit.github.io/doc/html/classttkPersistentGenerators.html).
For context, the one-dimensional separatrices of the MorseSmale complex are
computed using [MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html) and shown in the ParaView example.


The python script simply computes the generators and saves the result as a .vtp file.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/persistentGenerators_at.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/persistentGenerators_at.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/persistentGenerators_at.py
```


## Inputs
- [at.vti](https://github.com/topology-tool-kit/ttk-data/raw/dev/at.vti): A molecular dataset: a three-dimensional regular grid with 1 scalar field, the electronic density in the Adenine Thymine complex.

## Outputs
-  `PersistentGeneratorsAt.vtp`: the raw one-dimensional generators of the field.


## C++/Python API

[MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html)

[PersistentGenerators](https://topology-tool-kit.github.io/doc/html/classttkPersistentGenerators.html)
