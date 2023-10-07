# Interaction sites 

![Interaction sites example screenshot](https://topology-tool-kit.github.io/img/gallery/interactionSites.jpg)

## Pipeline description
This example demostrates how topological analysis can be used to identify interaction sites i.e. different kind of chemical bonds in molecules. Using simulations and experiments, the electron density field denoted as `Rho` can be estimated for a molecule. Topological analysis of this scalar field can reveal important features in the data. For example, the maxima of this field correspond to the atom locations while saddles occur along the covalent bonds. However, for identification of non-covalent interactions like ionic bonds, analysis of the density field `Rho` is not enough. A derived scalar field from `Rho` called [reduced density gradeint](https://www.tandfonline.com/doi/full/10.1080/00268976.2015.1123777) denoted by `s` is suggested in literature which can reveal non-covalent interation sites in a molecule. In this example, we will extract and compare the critical points for the `Rho` and `s` scalar fields for a simple molecule 1,2-ethanediol. 

First a VTI file is loaded which contains two scalar fields namely `log(Rho)` and `log(s)`. Then using [ScalarFieldCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldCriticalPoints.html), the critical points for `log(Rho)` are computed which are then converted into spheres using [IcospheresFromPoints](https://topology-tool-kit.github.io/doc/html/classttkIcospheresFromPoints.html). They are shown as bigger transluscent green and white spheres in the screenshot above. Note that these critical points identify the atoms and covalent bonds in the molecule.

Next, we analyse `log(s)`, the reduced gradient scalar field. Here, the [PersistenceCurve](https://topology-tool-kit.github.io/doc/html/classttkPersistenceCurve.html) is computed (top right view in the above screenshot). Then, the [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) for `log(s)` is computed and thresholds are applied based on persistence to maintain only the most persistent features. This results in a simplified persistence diagram (bottom right view in the above screenshot).

The simplified persistence diagram is then used as a constraint for the [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html) of the input scalar data. The simplified data is then used as input to [MergeTree](https://topology-tool-kit.github.io/doc/html/classttkMergeTree.html) to compute the join tree for the data. The join tree captures the topological changes in sub-level sets of the scalar field and therefore consists of leaves corresponding to minima and internal nodes corresponding to saddles, the points where sublevel sets merge. The nodes of this join tree are selected and highlighted as smaller opaque blue and white spheres using [IcospheresFromPoints](https://topology-tool-kit.github.io/doc/html/classttkIcospheresFromPoints.html). Similarly, the arcs of the join tree are also extracted and shown as thin grey tubes in the screenshot above.

Using topological analysis of `log(s)`, we identify an outlying minimum which is not close to the atom locations. This corresponds to a non-covalent interaction site in the molecule which is not identifiable using direct toplogical analysis of electron density field `Rho`. Lastly, we extract the segmented region corresponding to this particular minimum (shown as transluscent blue surface in the screenshot). 

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/interactionSites.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/interactionSites.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/interactionSites.py
```


## Inputs
- [BuiltInExample2.vti](https://github.com/topology-tool-kit/ttk-data/raw/dev/BuiltInExample2.vti): 3D scalar fields corresponding to electron density distribution `Rho` and the reduced density gradient `s` around a simple molecule 1,2-ethanediol.

## Outputs
- `logRhoCriticalPoints.vtp`: All the scalar field critical points computed for `log(Rho)`. 
- `logSPersistenceCurve.csv`: The output persistence curve for `log(s)`.
- `logSPersistenceDiagram.vtu`: The output persistence diagram for `log(s)`.
- `logSJoinTreeCriticalPoints.vtp`: The critical points in the join tree of `log(s)`.
- `logSJoinTreeArcs.vtp`: The arcs of the join tree of `log(s)`.
- `NonCovalentInteractionSite.vtp`: The non-covalent interaction site region identified using the join tree of `log(s)`.

Note that you are free to change the VTK file extensions to that of any other supported file format (e.g. `csv`) in the above python script.

## C++/Python API
[MergeTree](https://topology-tool-kit.github.io/doc/html/classttkMergeTree.html)

[GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html)

[IcospheresFromPoints](https://topology-tool-kit.github.io/doc/html/classttkIcospheresFromPoints.html)

[PersistenceCurve](https://topology-tool-kit.github.io/doc/html/classttkPersistenceCurve.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[ScalarFieldCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldCriticalPoints.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)
