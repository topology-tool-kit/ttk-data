# Merge Tree Temporal Reduction

![Merge Tree Temporal Reduction example Image](https://topology-tool-kit.github.io/img/gallery/mergeTreeTemporalReduction.jpg)

## Pipeline description
This example first loads an ensemble of scalar fields inside a single file from disk.
Then, the [Split Tree](https://topology-tool-kit.github.io/doc/html/classttkFTMTree.html) is computed on each scalar field.

All these trees are passed to [MergeTreeTemporalReductionEncoding](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeTemporalReductionEncoding.html) to compute a subsampling of a sequence of merge trees. The algorithm greedily removes trees in the sequence that can be accurately reconstructed by the geodesic computation. The remaining trees are called the key frames.

In terms of visualisation, the three key frames trees and two reconstructed trees are visualized with a planar layout along with their corresponding scalar fields.

The python script saves the information needed to reconstruct the trees removed in the sequence.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
$ paraview states/mergeTreeTemporalReduction.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/mergeTreeTemporalReduction.py"
```

## Inputs
- [isabel.vti](https://github.com/topology-tool-kit/ttk-data/raw/dev/isabel.vti): a three-dimensional regular grid with 12 scalar fields.

## Outputs
-  `ReductionCoefficients.csv`: a table containing information needed to reconstruct removed trees. For each removed tree we have the id of the two key frames needed to reconstruct it ('Index1' and 'Index2'), along with the interpolation parameter ('Alpha').


## C++/Python API
[FTMTree](https://topology-tool-kit.github.io/doc/html/classttkFTMTree.html)

[MergeTreeTemporalReductionEncoding](https://topology-tool-kit.github.io/doc/html/classttkMergeTreeTemporalReductionEncoding.html)

