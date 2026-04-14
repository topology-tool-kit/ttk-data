# Persistence Diagram Wasserstein Auto-Encoder 

![Persistence Diagram Wasserstein Auto-Encoder example Image](https://topology-tool-kit.github.io/img/gallery/persistenceDiagramWAE.jpg)


## Pipeline description
This example first loads an ensemble of scalar fields inside a cinema database from disk.
Then, the [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) is computed on each scalar field.

All these diagrams are passed to [MergeTreeAutoencoder](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeAutoencoder.html) to compute a wasserstein auto-encoding in the metric space of persistence diagrams. 

Then the filter [MergeTreeAutoencoderDecoding](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeAutoencoderDecoding.html) is used to reconstruct the input diagrams. 

In terms of visualization, a scalar field is displayed for each cluster. The original diagrams are displayed alongside their reconstruction at their right. The persistence pairs of the diagrams are colored by ID to see what features they correspond to in the scalar field.

The 2D planar layout is displayed with the persistence correlation view at the top right. The 12 scalar fields are colored by Cluster ID.

The python script computes the PD-WAE basis. This computation is not deterministic and it may take a minute  (depending on your hardware). It saves the resulting coefficients of the input diagrams and the axes of the bases and their origins. Finally it saves the reconstructed diagrams given the bases and the coordinates of the diagrams in the basis.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/persistenceDiagramWAEDecoding.pvsm
```

To reproduce the above analysis pipeline *as well as* the (non-deterministic) training procedure, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command (the computation may take a minute, depending on your hardware):
``` bash
paraview states/persistenceDiagramWAE.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/persistenceDiagramWAE.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/persistenceDiagramWAE.py
```

## Inputs
- [Isabel.cdb](https://github.com/topology-tool-kit/ttk-data/tree/dev/Isabel.cdb): a cinema database containing 12 regular grids.

## Outputs
-  `PD-WAE_processed_diagrams.vtm`: the processed input diagrams.
-  `PD-WAE_origins.vtm`: the origins of each basis.
-  `PD-WAE_axes.vtm`: the axes of each basis.
-  `PD-WAE_coef.vtm`: the coefficients of the input diagrams corresponding to their coordinates in each basis.
-  `PD-WAE_reconstructed_diagrams.vtm`: the reconstructed input diagrams.


## C++/Python API
[CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html)

[CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html)

[DataSetToTable](https://topology-tool-kit.github.io/doc/html/classttkDataSetToTable.html)

[IcospheresFromPoints](https://topology-tool-kit.github.io/doc/html/classttkIcospheresFromPoints.html)

[MergeTreeAutoencoder](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeAutoencoder.html)

[MergeTreeAutoencoderDecoding](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeAutoencoderDecoding.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)
