# Harmonic Skeleton 

![Harmonic Skeleton Image](https://topology-tool-kit.github.io/img/gallery/harmonicSkeleton.jpg)


## Pipeline description
This example first loads the pegasus triangle mesh from disk.
For pre-processing, an elevation function is computed on the mesh, creating Ids for all vertices afterwards.
From the created ids the bottom middle of the platform, both wing tips, the tip of the nose and the tip of the horn of pegasus are selected (right view shows them together with more vertices).

Now, a [HarmonicField](https://topology-tool-kit.github.io/doc/html/classttkHarmonicField.html) is computed using these five points as extrema in the output field, helping to reduce noise in the dataset, creating a smooth field with defined extrema that can later be extracted.

The harmonic field is then normalized using the [ScalarFieldNormalizer](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldNormalizer.html).

Then, the [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) is computed on the normalized field, extracting a threshold that is used to simplify the harmonic field using [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html).

Finally, the [ReebGraph](https://topology-tool-kit.github.io/doc/html/classttkReebGraph.html) is constructed, extracting its nodes and arcs afterwards (right view shows them). The arcs of the [ReebGraph](https://topology-tool-kit.github.io/doc/html/classttkReebGraph.html) are smoothed with the [GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html) to produce the final, output shape skeleton.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/harmonicSkeleton.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/harmonicSkeleton.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/harmonicSkeleton.py
```


## Inputs
- [pegasus.vtu](https://github.com/topology-tool-kit/ttk-data/raw/dev/pegasus.vtu): a two-dimensional triangulation.

## Outputs
- `ReebGraphNodes.vtp`: spheres, representing the nodes of the output [ReebGraph](https://topology-tool-kit.github.io/doc/html/classttkReebGraph.html)
in VTK file format (bottom right view, above screenshot). You are free to change the `vtp` file extension to that of any other supported file format (e.g. `csv`) in the above python script.
- `ReebGraphArcs.vtp`: cylinders (the output skeleton of the input shape), representing the arcs of the output [ReebGraph](https://topology-tool-kit.github.io/doc/html/classttkReebGraph.html)
in VTK file format (bottom right view, above screenshot). You are free to change the `vtp` file extension to that of any other supported file format (e.g. `csv`) in the above python script.

## C++/Python API
[ReebGraph](https://topology-tool-kit.github.io/doc/html/classttkReebGraph.html)

[GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html)

[HarmonicField](https://topology-tool-kit.github.io/doc/html/classttkHarmonicField.html)

[IcosphereFromPoints](https://topology-tool-kit.github.io/doc/html/classttkIcospheresFromPoints.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[ScalarFieldNormalizer](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldNormalizer.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)

