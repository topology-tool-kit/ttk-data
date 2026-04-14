# Contour Tree Alignment 

![CT bones example Image](https://topology-tool-kit.github.io/img/gallery/contourTreeAlignment.jpg)

## Pipeline description
This example first loads a scalar field ensemble from disk as a cinema data base.
The ensemble consists of 23 time-dependent scalar fields with 10 time steps each.
The ensemble is then filtered for the 23 scalar fields of one fixed time point and read as a vtkMultiBlockDataSet.
Here we use the [CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html), [CinemaQuery](https://topology-tool-kit.github.io/doc/html/classttkCinemaQuery.html) and [CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html) filters.

In a pre-processing, the scalar fields are topologically simplified by persistence using the [TopologicalSimplificationByPersistence](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplificationByPersistence.html) filter.
The filter is automatically applied to each member of the MultiBlockDataSet.
Then, for each simplified member field, the contour tree is computed using the [ContourTree](https://topology-tool-kit.github.io/doc/html/classttkContourTree.html) module.

The resulting MultiBlock of contour trees is then used as input for the [Contour Tree Alignment](https://topology-tool-kit.github.io/doc/html/classttkContourTreeAlignment.html) filter.
This alignment is a super tree of all contour trees and can be seen as a representative of the topology of the whole ensemble.
Unfortunately, the vtk object representing the alignment does not have any layout information attached.
Therefore, we use the [PlanarGraphLayout](https://topology-tool-kit.github.io/doc/html/classttkPlanarGraphLayout.html) together with a paraview calculator to compute and apply the layout information.

We now want to check which features of the original scalar fields have been matched onto each other.
Therefore, we use the `ExtractSeletion` filter to extract one vertex and attach its `segmentationIDs` array to the multi block data set representing the segmentations of the contour trees.
We also use a [Grid Layout](https://topology-tool-kit.github.io/doc/html/classttkGridLayout.html) to render the multi block in a comparable fashion (right view, above screenshot).

As a last step, we use the [ForEach](https://topology-tool-kit.github.io/doc/html/classttkForEachhtml) and [EndFor](https://topology-tool-kit.github.io/doc/html/classttkEndFor.html) filters to iterate the multi block of segmentations and in each iteration, we extract the region of the scalar field that corresponds to the segmentation id from the selected vertex.
The extraction is done using the [TTKExtract](https://topology-tool-kit.github.io/doc/html/classttkExtract.html) filter.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/contourTreeAlignment.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/contourTreeAlignment.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/contourTreeAlignment.py
```


## Inputs
- [heatedCylinder/heatedCylinder_2D_raw.cdb](https://github.com/topology-tool-kit/ttk-data/raw/dev/heatedCylinder/heatedCylinder_2D_raw.cdb): a cinema data base of 23x10 2D scalar fields.

## Outputs
- `ContorTreeAlignment.vtu`: the output alignment in VTK file format (left view, above screenshot).
- `Segmentations.vtm`: the segmentations of the input scalar fields in VTK multiblock format (right view, above screenshot).
- `MatchedRegions.vtm`: the regions of the original fields that are represented by a selected vertex in VTK multiblock format (right view, abſove screenshot).


## C++/Python API
[ArrayEditor](https://topology-tool-kit.github.io/doc/html/classttkArrayEditor.html)

[BlockAggregator](https://topology-tool-kit.github.io/doc/html/classttkBlockAggregator.html)

[CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html)

[CinemaQuery](https://topology-tool-kit.github.io/doc/html/classttkCinemaQuery.html)

[CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html)

[ContourTree](https://topology-tool-kit.github.io/doc/html/classttkContourTree.html)

[ContourTreeAlignment](https://topology-tool-kit.github.io/doc/html/classttkContourTreeAlignment.html)

[EndFor](https://topology-tool-kit.github.io/doc/html/classttkEndFor.html)

[Extract](https://topology-tool-kit.github.io/doc/html/classttkExtract.html)

[ForEach](https://topology-tool-kit.github.io/doc/html/classttkForEach.html)

[GridLayout](https://topology-tool-kit.github.io/doc/html/classttkGridLayout.html)

[PlanarGraphLayout](https://topology-tool-kit.github.io/doc/html/classttkPlanarGraphLayout.html)

[TopologicalSimplificationByPersistence](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplificationByPersistence.html)

