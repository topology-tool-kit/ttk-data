# CT bones 

![CT bones example Image](https://topology-tool-kit.github.io/img/gallery/ctBones.jpg)

## Pipeline description
This example segments medical image data based on topological persistence.

First, the [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) of the data is computed (top right view, above screenshot). 

Then, only the 5 most persistent maxima are selected, corresponding to the toes of the foot.

Next, the input data is simplified based on the selected persistent features, via [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html).

Next, the [Split tree](https://topology-tool-kit.github.io/doc/html/classttkMergeTree.html) of the simplified data is computed. 

Finally, the geometry of the bones of the toes is extracted by selecting the regions (in the 3D data) attached to the leaves (`RegionType` equals 1) of the [Split tree](https://topology-tool-kit.github.io/doc/html/classttkMergeTree.html) (center view, above screenshot).

To get a refined segmentation, change the persistence threshold from `180` down to `150`. 
Each toe will be subdivided into two segments, precisely along the joints.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/ctBones.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/ctBones.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/ctBones.py
```


## Inputs
- [ctBones.vti](https://github.com/topology-tool-kit/ttk-data/raw/dev/ctBones.vti): a three-dimensional regular grid encoding material density in a medical image (CT scan).

## Outputs
- `CTBonesOutputSegmentation.vtu`: the geometry of the volume of the bones of the toes, as extracted by the analysis pipeline (most persistent super-level set connected components).

## C++/Python API
[MergeTree](https://topology-tool-kit.github.io/doc/html/classttkMergeTree.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)

