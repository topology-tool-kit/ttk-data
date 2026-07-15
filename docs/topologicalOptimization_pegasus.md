# Topological Optimization for Pegasus Genus Repair

![Topological Optimization Pegasus example Image](https://topology-tool-kit.github.io/img/gallery/topologicalOptimizationPegasus.jpg)

## Pipeline description
This example simplifies a handle defect on an acquired surface geometry (pegasus statue) via the topological optimization of a [SignedDistanceField](https://topology-tool-kit.github.io/doc/html/classttkSignedDistanceField.html) to the input surface.

The processing pipeline first loads the surface and clips it to extract the handle defect.
It then computes a signed distance field to create a scalar field defined on a regular grid using the [SignedDistanceField](https://topology-tool-kit.github.io/doc/html/classttkSignedDistanceField.html) module.
The persistence diagram is computed using the [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) module and then it is thresholded to create a target diagram where the persistence pair corresponding to the handle defect is removed.
Finally, using the topological optimization backend of [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html), the pipeline optimizes the scalar field to remove the handle defect from the level set corresponding to the considered surface. This removal is exemplified with the cutting (bottom left) and filling (bottom right) strategies.

Note that the handle defect can be detected by identifying the [PersistentGenerators](https://topology-tool-kit.github.io/doc/html/classttkPersistentGenerators.html) of smallest size. In this example, the [PersistentGenerators](https://topology-tool-kit.github.io/doc/html/classttkPersistentGenerators.html) are computed out of a low resolution signed distance field (to make the example easily computable). To detect the handle defect, a higher resolution is required (typically `1024^3` -- expect hours of computation -- but then TTK needs to be built with 64 bit identifiers, `TTK_ENABLE_64BIT_IDS=ON`).

The python script computes the topological optimization and saves the optimized scalar fields with the cutting and the filling strategies.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/topologicalOptimization_pegasus.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/topologicalOptimization_pegasus.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/topologicalOptimization_pegasus.py
```

## Inputs
- [pegasus.vtu](https://github.com/topology-tool-kit/ttk-data/raw/dev/pegasus.vtu): An acquired surface geometry representing a pegasus statue.

## Outputs
-  `topoOpt_pegasus_fill.vti`: the optimized dataset with the fill strategy.
-  `topoOpt_pegasus_cut.vti`: the optimized dataset with the cut strategy.

## C++/Python API

[GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[PersistentGenerators](https://topology-tool-kit.github.io/doc/html/classttkPersistentGenerators.html)

[ScalarFieldSmoother](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldSmoother.html)

[SignedDistanceField](https://topology-tool-kit.github.io/doc/html/classttkSignedDistanceField.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)
