# Contour Tree Alignment example

![CT bones example Image](https://topology-tool-kit.github.io/img/gallery/contourTreeAlignment.jpg)

## Pipeline description
This example first loads a scalar field ensemble from disk as a cinema data base.
The ensemble consists of 23 time-dependent scalar fields with 10 time steps each.
The ensemble is then filtered for the 23 scalar fields of one fixed time point and read as a vtkMultiBlockDataSet.
Here we use the [CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html), [CinemaQuery](https://topology-tool-kit.github.io/doc/html/classttkCinemaQuery.html) and [CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html) filters.

In a pre-processing, the scalar fields are topologically simplified by persistence using the [TopologicalSimplificationByPersistence](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplificationByPersistence.html) filter.
The filter is automatically applied to each member of the MultiBlockDataSet.
Then, for each simplified member field, the contour tree is computed using the [FTMTree](https://topology-tool-kit.github.io/doc/html/classttkFTMTree.html) module.

The resulting MultiBlock of contour trees is then used as input for the [Alignment](https://topology-tool-kit.github.io/doc/html/classttkContourTreeAlignment.html) filter.
This alignment is a super tree of all contour trees and can be seen as a representative of the topology of the whole ensemble.
Unfortunately, the vtk object representing the alignment does not have any layout information attached.
Therefore, we use the [PlanarGraphLayout](https://topology-tool-kit.github.io/doc/html/classttkPlanarGraphLayout.html) together with a paraview calculator to compute and apply the layout information.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
$ paraview states/contourTreeAlignmentWithMatching.pvsm
```

To only get the left view, enter the following command instead:
``` bash
$ paraview states/contourTreeAlignment.pvsm
```

## Python code
The following python code will produce the alignment (left view, above screenshot) as a vtk file.

``` python  linenums="1"
--8<-- "python/contourTreeAlignment.py"
```

## Inputs
- [heatedCylinder/heatedCylinder_2D_raw.cdb](https://github.com/topology-tool-kit/ttk-data/raw/dev/heatedCylinder/heatedCylinder_2D_raw.cdb): a cinema data base of 23x10 2D scalar fields.

## Outputs
- `ContorTreeAlignment.vtu`: the output alignment in VTK file format (left view, above screenshot).


## C++/Python API
[CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html)

[CinemaQuery](https://topology-tool-kit.github.io/doc/html/classttkCinemaQuery.html)

[CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html)

[TopologicalSimplificationByPersistence](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplificationByPersistence.html)

[ContourTree (FTM)](https://topology-tool-kit.github.io/doc/html/classttkFTMTree.html)

[Alignment](https://topology-tool-kit.github.io/doc/html/classttkContourTreeAlignment.html)

[PlanarGraphLayout](https://topology-tool-kit.github.io/doc/html/classttkPlanarGraphLayout.html)

