# Topological Optimization DarkSky

![Topological Optimization DarkySky example Image](https://topology-tool-kit.github.io/img/gallery/topologicalOptimization_darkSky.png)

## Pipeline description
This example simplifies all the persistence pairs below 25% of the maximum persistence of the density of dark matter in an astrophysics simulation.

This example first loads the point cloud then applies a gaussian resampling to create a scalar field defined on a regular grid.
Then the scalar field is smoothed with [ScalarFieldSmoother](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldSmoother.html) (with 5 iterations).
The persistence diagram is computed using [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) and then thresholded to create a target diagram where the persistence pairs having persistence below 25% of the maximum persistence are removed.
Finally, using the topological optimization backend of [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html), it optimizes the scalar field to remove, as much as possible, the pairs which are not in the target diagram.

The python script computes the topological optimization and saves the optimized scalar field.

Note that the optimization will take a long time (typically, around 40 minutes). For interactive visualization purposes, we suggest to first run the optimization in batch mode with `pvpython` (see [instructions below](#python-code)) and then run the post-process visualization state `topologicalOptimization_darkSky_postProcess.pvsm` (see [instructions below](#paraview)).

## ParaView
To reproduce the above screenshot (and run the optimization online, around 40 minutes), go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/topologicalOptimization_darkSky.pvsm
```

If you have already computed the optimization with `pvpython`  (see [instructions below](#python-code)), simply enter:
``` bash
paraview states/topologicalOptimization_darkSky_postProcess.pvsm
```


## Python code

``` python  linenums="1"
--8<-- "python/topologicalOptimization_darkSky.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command (around 40 minutes of runtime):
``` bash
pvpython python/topologicalOptimization_darkSky.py
```

## Inputs
- [ds14_scivis_0128_e4_dt04_1.0000.vtp](https://github.com/topology-tool-kit/ttk-data/raw/dev/ds14_scivis_0128_e4_dt04_1.0000.vtp): A point cloud dataset representing a simulation of the density of dark matter in the universe.

## Outputs
-  `darkSky_optimized.vti`: the optimized dataset.

## C++/Python API

[MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[ScalarFieldSmoother](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldSmoother.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)
