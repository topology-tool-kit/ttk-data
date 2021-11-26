# Harmonic Skeleton example

![Harmonic Skeleton Image](https://topology-tool-kit.github.io/img/gallery/harmonicSkeleton.jpg)


## Pipeline description
This example first loads the pegasus triangle mesh from disk.
For pre-processing, an elevation function is computed on the mesh, creating Ids for all vertices afterwards.
From the created ids the bottom middle of the platform, both wing tips, the tip of the nose and the tip of the horn of pegasus are selected(right view shows them together with more vertices).

Now, a [TTKHarmonicField](https://topology-tool-kit.github.io/doc/html/classttkHarmonicField.html) is computed using these five points as extrema in the output field, helping to reduce noise in the dataset, creating a smooth field with defined extrema that can later be extracted.

The harmonic field is then normalized using the [TTKScalarFieldNormalizer](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldNormalizer.html).

Then, the [TTKPersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) is computed on the normalized field, extracting a threshold that is used to simplify the harmonic field using [TTKTopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html).

Finally, the [FTRGraph](https://topology-tool-kit.github.io/doc/html/classttk_1_1ftr_1_1FTRGraph.html) is constructed, extracting its nodes and arcs afterwards(right view shows them)

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
$ paraview states/harmonicSkeleton.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/harmonicSkeleton.py"
```

## Inputs
- [pegasus.vtu](https://github.com/topology-tool-kit/ttk-data/raw/dev/pegasus.vtu): a two-dimensional triangulation.

## Outputs
- `ReebGraphNodes.vtp`: spheres, representing the nodes of the output FTRGraph
in VTK file format (bottom right view, above screenshot). You are free to change the `vtp` file extension to that of any other supported file format (e.g. `csv`) in the above python script.
- `ReebGraphArcs.vtp`: cylinders, representing the arcs of the output FTRGraph
in VTK file format (bottom right view, above screenshot). You are free to change the `vtp` file extension to that of any other supported file format (e.g. `csv`) in the above python script.

## C++/Python API
[TTKHarmonicField](https://topology-tool-kit.github.io/doc/html/classttkHarmonicField.html)

[TTKScalarFieldNormalizer](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldNormalizer.html)

[TTKPersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[TTKTopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)

[FTRGraph](https://topology-tool-kit.github.io/doc/html/classttk_1_1ftr_1_1FTRGraph.html)
