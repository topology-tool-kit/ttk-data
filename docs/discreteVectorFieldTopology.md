# Discrete Vector Field Topology

![Discrete Vector Field Topology Result Image](https://topology-tool-kit.github.io/img/gallery/discreteVectorFieldTopology.jpg)

## Pipeline description
This example computes the critical points, separatrices, and segmentation of a simplified vector field with added noise and threshold determined by the associated weight curve.

First, the vector field data is added with a random vector of size 0.3. 

Then, the [VectorWeightCurve](https://topology-tool-kit.github.io/doc/html/classttkVectorWeightCurve.html) is computed.
The output is the simplified pairs and the weight associated with each pair.
We use this curve to determine stable/flat regions to simplify to.
Looking at the displayed weight curve (using log scales), we see a good (flat) spot to simplify to at 27 critical points.

Next, the input data is simplified based on the selected threshold (27 critical points), via [TopologicalSkeleton](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSkeleton.html) and using [VectorSimplification](https://topology-tool-kit.github.io/doc/html/classVectorSimplification.html) on the backend.

Finally, the Critical Points and Separatrices are computed then displayed and
the `Intersecting Manifold` segmentation is shown (with a random color per
manifold, by using [IdentifierRandomizer](https://topology-tool-kit.github.io/doc/html/classttkIdentifierRandomizer.html)).

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/discreteVectorFieldTopology.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/discreteVectorFieldTopology.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/discreteVectorFieldTopology.py
```

## Inputs
- [changes.vtu](https://github.com/topology-tool-kit/ttk-data/raw/dev/changes.vtu): a two-dimensional regular grid encoding flow of a piecewise implicit function.

## Outputs
- `WeightCurve.csv`: the plot of pairs according to weight and total number of critical points remaining in the simplified field.
- `CriticalPoints.csv`: the critical points of the simplified [DiscreteVectorField](https://topology-tool-kit.github.io/doc/html/classttkDiscreteVectorField.html).
- `Separatrices1.csv`: the output separatrices traced along the saddles (critical simplices of dimension 1) on the simplified field.
- `Segmentation.vtu`: the output segmentation in VTK file format. The segmentation is stored as point data with segment numbers associated with common flow patterns(descending, ascending, and intersecting). 

## C++/Python API
[VectorWeightCurve](https://topology-tool-kit.github.io/doc/html/classttkVectorWeightCurve.html)

[TopologicalSkeleton](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSkeleton.html)

[VectorSimplification](https://topology-tool-kit.github.io/doc/html/classVectorSimplification.html)

[DiscreteVectorField](https://topology-tool-kit.github.io/doc/html/classttkDiscreteVectorField.html)


