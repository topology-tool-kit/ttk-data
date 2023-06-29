# Nested Tracking From Overlap

![Nested tracking graph
screenshot](https://topology-tool-kit.github.io/img/gallery/nestedTrackingGraph.jpg)

## Pipeline description
This example first opens the viscous fingering cinema database via the `ttkCinemaReader`, and then queries all entries of one specific simulation run ordered by time via the `ttkCinemaQuery` filter.
Then the pipeline iterates over the resulting database entries via the `ttkForEach` and `ttkEndFor` filters, and loads the corresponding data product of each iteration with the `ttkCinemaProductReader`.
Then the script computes three superlevel sets for the levels 20, 28, and 32 via three separate `Threshold` filters.
Next the pipeline computs the connected components of these sets via the `Connectivity` filter.
Then the components are packaged into a specific `vtkMultiBlockDataSet` hierrachy via `ttkBlockAggregator` filters, and this structure is then fed sequentially into the `ttkTrackingFromOverlap` filter which computes the overlap of the components across time and levels.
After all iterations, the `ttkTrackingFromOverlap` filter will produce the resulting nested tracking graph.
The `ttkPlanarGraphLayout` filter then computes an optimized layout for the NTG, where the actual transformation of the graph coordinates is applied in the following `Calculator` filter.
Finally the `ttkMeshGraph` filter generates a `vtkUnstructuredGrid` of the NTG with dynamic edge widths, which is then stored to disk.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/nestedTrackingFromOverlap.py
```

## Python code

``` python  linenums="1"
--8<-- "python/nestedTrackingFromOverlap.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/nestedTrackingFromOverlap.py
```


## Inputs
- [ViscousFingers.cdb](https://github.com/topology-tool-kit/ttk-data/ViscousFingers.cdb): a cinema database containing 3D volume data of salt concentrations.

## Outputs
- `NTG.vtu`: the meshed nested tracking graph of superlevel set components for the levels 20, 28, and 32.

## C++/Python API

[ArrayEditor](https://topology-tool-kit.github.io/doc/html/classttkArrayEditor.html)


[BlockAggregator](https://topology-tool-kit.github.io/doc/html/classttkBlockAggregator.html)


[CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html)

[CinemaQuery](https://topology-tool-kit.github.io/doc/html/classttkCinemaQuery.html)

[CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html)

[EndFor](https://topology-tool-kit.github.io/doc/html/classttkEndFor.html)


[ForEach](https://topology-tool-kit.github.io/doc/html/classttkForEach.html)

[MeshGraph](https://topology-tool-kit.github.io/doc/html/classttkMeshGraph.html)

[PlanarGraphLayout](https://topology-tool-kit.github.io/doc/html/classttkPlanarGraphLayout.html)

[TrackingFromOverlap](https://topology-tool-kit.github.io/doc/html/classttkTrackingFromOverlap.html)

