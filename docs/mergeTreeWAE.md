# Merge Tree Wasserstein Auto-Encoder

![Merge Tree Wasserstein Auto-Encoder example Image](https://topology-tool-kit.github.io/img/gallery/mergeTreeWAE.jpg)


## Pipeline description
This example first loads an ensemble of scalar fields inside a cinema database from disk.
Then, the [MergeTree](https://topology-tool-kit.github.io/doc/html/classttkMergeTree.html) is computed on each scalar field to compute the Split Tree.

All these trees are passed to [MergeTreeAutoencoder](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeAutoencoder.html) to compute a wasserstein auto-encoding in the metric space of merge trees. 

Then the filter [MergeTreeAutoencoderDecoding](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeAutoencoderDecoding.html) is used to reconstruct the input merge trees. 

In terms of visualization, a scalar field is displayed for each cluster, with a zoom on their right of the important persistence pairs. The original merge trees are displayed alongside their reconstruction at their right. The persistence pairs of the trees are colored by ID to see what features they correspond to in the scalar field.

The 2D planar layout is displayed with the persistence correlation view at the top right. The 12 scalar fields are colored by Cluster ID. Finally, a path drawn with PolyLineSource on the layout is drawn at the bottom right to show how we can interactivily explore the MT-WAE latent space with user-defined locations.

The python script computes the MT-WAE basis. This computation is not deterministic and it may take several minutes (depending on your hardware). It saves the resulting coefficients of the input merge trees and the axes of the bases and their origins. Finally it saves the reconstructed merge trees given the bases and the coordinates of the merge trees in the basis.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/mergeTreeWAEDecoding.pvsm
```

To reproduce the above analysis pipeline *as well as* the (non-deterministic) training procedure, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command (the computation will take several minutes, depending on your hardware):
``` bash
paraview states/mergeTreeWAE.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/mergeTreeWAE.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/mergeTreeWAE.py
```

## Inputs
- [Earthquake.cdb](https://github.com/topology-tool-kit/ttk-data/tree/dev/Earthquake.cdb): a cinema database containing 12 regular grids.

## Outputs
-  `MT-WAE_processed_diagrams.vtm`: the processed input merge trees.
-  `MT-WAE_origins.vtm`: the origins of each basis.
-  `MT-WAE_axes.vtm`: the axes of each basis.
-  `MT-WAE_coef.vtm`: the coefficients of the input merge trees corresponding to their coordinates in each basis.
-  `MT-WAE_reconstructed_diagrams.vtm`: the reconstructed input merge trees.


## C++/Python API
[ArrayEditor](https://topology-tool-kit.github.io/doc/html/classttkArrayEditor.html)

[BlockAggregator](https://topology-tool-kit.github.io/doc/html/classttkBlockAggregator.html)

[CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html)

[CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html)

[DataSetToTable](https://topology-tool-kit.github.io/doc/html/classttkDataSetToTable.html)

[FlattenMultiBlock](https://topology-tool-kit.github.io/doc/html/classttkFlattenMultiBlock.html)

[GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html)

[IcospheresFromPoints](https://topology-tool-kit.github.io/doc/html/classttkIcospheresFromPoints.html)

[MergeTree](https://topology-tool-kit.github.io/doc/html/classttkMergeTree.html)

[MergeTreeAutoencoder](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeAutoencoder.html)

[MergeTreeAutoencoderDecoding](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeAutoencoderDecoding.html)

[MergeTreeClustering](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeClustering.html)

