# Uncertain Starting Vortex 

<!--[![Uncertain Starting Vortex example video tutorial](https://topology-tool-kit.github.io/img/gallery/uncertainStartingVortex.jpg)](https://youtu.be/18sxV6A5REA)-->

<iframe width="100%" height="420"
src="https://www.youtube.com/embed/18sxV6A5REA" frameborder="0"
allowfullscreen></iframe>

## Pipeline description
This example loads an uncertain 2D wing simulation (obtained from an ensemble simulation). This input data contains the upper and lower bounds for the simulation results as two separate scalar fields.

Using both fields, the [MandatoryCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkMandatoryCriticalPoints.html), representing areas that are guaranteed to locate a critical point of the selected type in any possible realization, are computed (both left views show them as areas in blue for minima and green for maxima).

A realization of the simulation is created by using a normalized random scalar field, interpolating between the lower and upper bound using the random scalar at each point. 

As this process introduces noise, a [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html) is created (both right views).

From it, first all point pairs are extracted, then retrieving a persistence threshold that is used as a constraint for the [TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html) to filter the introduced noise.

At last, the [ScalarFieldCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldCriticalPoints.html) (top left view, above screenshot) are computed for the smoothed realization (both left views show them as spheres). The critial points extracted from this random realization are indeed located within the regions predicted by the [MandatoryCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkMandatoryCriticalPoints.html).


## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/uncertainStartingVortex.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/uncertainStartingVortex.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/uncertainStartingVortex.py
```


## Inputs
- [uncertainStartingVortex.vti](https://github.com/topology-tool-kit/ttk-data/raw/dev/uncertainStartingVortex.vti): two two-dimensional scalar fields.

## Outputs

- `PersistenceDiagram.vtu`: the output persistence diagram in VTK file format (bottom right view, above screenshot). You are free to change the `vtu` file extension to that of any other supported file format (e.g. `csv`) in the above python script.
- `CriticalPoints.vtp`: the output
critical points
in VTK file format (bottom right view, above screenshot). You are free to change the `vtp` file extension to that of any other supported file format (e.g. `csv`) in the above python script.
- `MandatoryCriticalMinima.csv`: the output mandatory critical minima points (both left views, blue areas).
- `MandatoryCriticalMaxima.csv`: the output mandatory critical maxima points (both left views, green areas).


## C++/Python API

[MandatoryCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkMandatoryCriticalPoints.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[ScalarFieldCriticalPoints](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldCriticalPoints.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)


