# Topological Optimization for Torus Genus Repair

![Topological Optimization Torus example Image](https://topology-tool-kit.github.io/img/gallery/topologicalOptimizationTorus.jpg)

## Pipeline description
This toy example simplifies the handle of a torus via the topological optimization of a [SignedDistanceField](https://topology-tool-kit.github.io/doc/html/classttkSignedDistanceField.html) to the input surface.

This processing pipeline first loads the surface.
Then, it computes a signed distance field to create a scalar field defined on a regular grid using the [SignedDistanceField](https://topology-tool-kit.github.io/doc/html/classttkSignedDistanceField.html) module.
The persistence diagram is computed using the [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) module and then it is thresholded to create a target diagram where only the persistence pair with infinite persistence is kept.
Finally, using the topological optimization backend of [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html), the pipeline optimizes the scalar field to remove the handle. This removal is exemplified with the cutting (bottom left) and filling (bottom right) strategies.

The python script computes the topological optimization and saves the output surfaces (for the cutting and filling strategies).

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/topologicalOptimization_torus.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/topologicalOptimization_torus.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/topologicalOptimization_torus.py
```

## Inputs
- [torus.vtu](https://github.com/topology-tool-kit/ttk-data/raw/dev/torus.vtu): A surface representing a torus.

## Outputs
-  `topoOpt_torus_fill.vtp`: the repaired surface with the fill strategy.
-  `topoOpt_torus_cut.vtp`: the repaired surface with the cut strategy.

## C++/Python API

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[SignedDistanceField](https://topology-tool-kit.github.io/doc/html/classttkSignedDistanceField.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)

