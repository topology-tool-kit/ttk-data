# Builtin example 2

<!--[![Builtin example 2 video tutorial](https://topology-tool-kit.github.io/img/gallery/builtinExample2.jpg)](https://youtu.be/Rdsfkb6SpK8)-->

<iframe src="https://www.youtube.com/embed/7mlUzUJKA78" allowfullscreen="" width="100%" height="420" frameborder="0"></iframe>

## Pipeline description
This example demostrates how bivariate analysis can be used for the analysis of molecular data. The input to this pipeline are two scalar fields: the electron density field denoted as `log(Rho)` and the [reduced density gradeint](https://www.tandfonline.com/doi/full/10.1080/00268976.2015.1123777) denoted by `log(s)` for a simple molecule called 1,2-ethanediol.

First, usual univariate scalar field analysis method is used for the analysis. An isosurafce is extracted in `log(Rho)` field which helps in identification of the location of atoms in the molecule, see black surfaces in the lower left panel of the screenshot above. Similarly, an isosurafce in `log(s)` identifies the covalent bonds.

Next we perform bivariate analysis which looks at the joint behaviour `log(Rho)` and `log(s)` rather than looking at these scalar fields individually. We first compute the [ContinuousScatterPlot](https://topology-tool-kit.github.io/doc/html/classttkContinuousScatterPlot.html) for this bivariate data. This is shown in the top panel of the screenshot above. We then project the isosrfaces extrated earlier during univariate analysis in the range space using [ProjectionFromField](https://topology-tool-kit.github.io/doc/html/classttkProjectionFromField.html). As expected these isosurfaces project to two line segments which are perpendicular to each other and parallel to the X axis and Y axis, repectively.

Note how the continuous scatter plot spreads largely diagonally down from top-left corner to bottom-right in the range space with four distinct protrusions coming out on the top and bottom. These protrusions are of interest. We manually select polylines in the range space at these four protrusions and use them for extraction of fiber surfaces using [FiberSurface](https://topology-tool-kit.github.io/doc/html/classttkFiberSurface.html). 

Two of the fiber surfaces correspond to the atoms in the molecule, one of which identifies the Oxygen atoms (red surfaces in bottom right panel of the screenshot) while the other surface identifies the Carbon atoms (grey surfaces in bottom right panel of the screenshot). The other two fiber surfaces identify the bonds or interaction sites in the molecule. One surface clearly identifies the covalent bonds (blue surfaces in bottom right panel of the screenshot), while the other identifies a non-covalent interaction site in the molecule (light green surface in bottom right panel of the screenshot). Note that using univariate analysis of the data it is not straightforward to distinguish between different type of atoms and different types of bonds. However, it is much easier to do so using bivariate data analysis.

Lastly, we also compute the [JacobiSet](https://topology-tool-kit.github.io/doc/html/classttkJacobiSet.html) for the bivariate data and project it in the range space. Notice how it aligns with the continuous scatter plot and identifies the boundaries and the distinguishable curves within it.

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/BuiltInExample2.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/builtInExample2.py"
```

## Inputs
- [BuiltInExample2.vti](https://github.com/topology-tool-kit/ttk-data/raw/dev/BuiltInExample2.vti): Bivariate field corresponding to electron density distribution `log(Rho)` and the reduced density gradient `log(s)` around a simple molecule 1,2-ethanediol.

## Outputs

### Univariate analysis outputs
- `logRhoIsosurfaceAtoms.vtp`: An isosurface extracted from `log(Rho)` scalar field which identifies the locations of the atoms.
- `logSIsosurfaceBonds.vtp`: An isosurface extracted from `log(s)` scalar field which identifies the locations of the bonds or interaction sites.

### Bivariate analysis outputs 
#### Continuous scatter plot and projection of isocontours
- `ContinuousScatterPlot.vtu`: The continuous scatter plot for the `log(Rho)` and `log(s)` bivariate field.
- `logRhoIsosurfaceRangeProjection.vtp`: The projection of the isosurface extracted from `log(Rho)` onto the bivariate range space.
- `logSIsosurfaceRangeProjection.vtp`: The projection of the isosurface extracted from `log(s)` onto the bivariate range space.

#### Interesting control polygons in range space
- `OxygenAtomsRangePolygon.vtp`: Manually specified control polygon in range space to select the two Oxygen atoms in the molecule.
- `CarbonAtomsRangePolygon.vtp`: Manually specified control polygon to select the Carbon atoms in the molecule.
- `CovalentBondsRangePolygon.vtp`: Manually specified control polygon to identify the covalent bonds in the molecule.
- `NonCovalentIntercationSiteRangePolygon.vtp`: Manually specified control polygon to identify the non-covalent interaction sites in the molecule.

#### Corresponding fiber surfaces in spatial domain
- `OxygenAtomsFiberSurface.vtp`: The corresponding fiber surface in the spatial domain for the Oxygen atom control polygon.
- `CarbonAtomsFiberSurface.vtp`: The corresponding fiber surface in the spatial domain for the Carbon atom control polygon.
- `CovalentBondsFiberSurface.vtp`: The corresponding fiber surface in the spatial domain for the covalent bonds control polygon.
- `NonCovalentIntercationSiteFiberSurface.vtp`: The corresponding fiber surface in the spatial domain for the non-covalent bonds control polygon.

#### Jacobi set projection onto the continuous scatter plot 
- `JacobiSetRangeProjection.vtu`: The projection of the Jacobi set of the bivariate field onto the bivariate range space.

Note that you are free to change the VTK file extensions to that of any other supported file format (e.g. `csv`) in the above python script.


## C++/Python API
[ContinuousScatterPlot](https://topology-tool-kit.github.io/doc/html/classttkContinuousScatterPlot.html)

[FiberSurface](https://topology-tool-kit.github.io/doc/html/classttkFiberSurface.html)

[JacobiSet](https://topology-tool-kit.github.io/doc/html/classttkJacobiSet.html)

[ProjectionFromField](https://topology-tool-kit.github.io/doc/html/classttkProjectionFromField.html)


