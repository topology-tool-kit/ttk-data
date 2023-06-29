# Clustering Kelvin Helmholtz Instabilities

<iframe width="100%" height="420"
src="https://www.youtube.com/embed/EROXnZ5MuU0" frameborder="0"
allowfullscreen></iframe>

## Pipeline description
This example illustrates the capabilities of 
[TTK](https://topology-tool-kit.github.io/) to perform advanced statistical 
analysis of collections of datasets, based on their structural representations, 
along with the possibility to interactively explore the outcome of the analysis, 
with linked views (between the selection in the planar view -- top right -- and 
the flow visualization -- top left).

This example considers an ensemble of 32 periodic, 2D Kelvin Helmholtz 
Instabilities in computational fluid dynamics, obtained with various simulation 
parameters (different solvers, different numerical schemes, different 
interpolation orders, etc.). 
The scalar field of interest is the "Enstrophy". It is an established measure 
of vorticity. Its prominent maxima denote the center of strong vortices.
Two example members from 
the ensemble are show on the above screenshot (left). Strong vortices can be 
visualized with the dark green regions.
The simulation parameters as well as the ground truth classification are 
provided as metadata for each entry of the database and are carried along the 
entire pipeline.
See this [publication](https://arxiv.org/abs/2207.14080) for 
further details.

The goal of this example is to classify the 32 members of the ensemble into two 
classes, whether they 
describe
the beginning or the end of 
the turbulence. This task is particularly challenging for traditional 
clustering pipelines since turbulent flows are highly chaotic and two flows 
belonging to the same ground truth class can be drastically different visually 
(as shown on the above screenshot -- left). The common denominator between two 
turbulent flows in the same ground truth class is the distribution of energies 
of their vortices (i.e. the number and strengths of their vortices), which 
describes the turbulence of the flow.

In this context, topological data representations are particularly relevant to 
extract such subtle structural features. In particular, the persistence diagram 
involving the saddle-maximum pairs of the "Enstrophy" (second column, above 
screenshot) nicely captures the number of vortices as well as their individual 
strengths. Thus, in the reminder of this example, we will use this persistence 
diagram as a descriptor of each turbulent flow and we will proceed to a k-means 
clustering directly in the Wasserstein metric space of persistence diagrams. 
For visualization purposes, we will compute a 2D layout of the ensemble (right 
most columns, above screenshot) to inspect the resulting classification.

First, the database of turbulent flows is loaded from disk with the 
[CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html)
module (line 6 of the [Python](#python-code) script below). Then an SQL 
query is performed with 
[CinemaQuery](https://topology-tool-kit.github.io/doc/html/classttkCinemaQuery.html)
to select a relevant subset of this database (line 9). Finally the module 
[CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html)
is used to read the actual regular grids 
corresponding to the result of the previous SQL query. From this point on, the 
entire set of 32 turbulent flows will be organized as a 
[vtkMultiBlockDatSet](https://vtk.org/doc/nightly/html/classvtkMultiBlockDataSet.html)
and each of these 32 members will be processed by the rest of the 
analysis pipeline.

Then for each of the 32 members of the ensemble, the first step consists in 
marking periodicity boundary conditions with the 
[TriangulationManager](https://topology-tool-kit.github.io/doc/html/classttkTriangulationManager.html) 
(line 21). Next, the "Enstrophy" field of 
each member is normalized (between 0 and 1) with the 
[ScalarFieldNormalizer](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldNormalizer.html)
to ease their comparison later. Finally 
(line 28) the 
[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)
is computed (for the saddle-maximum pairs) to 
represent each of the 32 ensemble members by a diagram which encodes the number 
and the strengths of the vortices via the persistence of the maxima of 
"Enstrophy".

Next, the clustering of the persistence diagrams in the Wasserstein metric 
space is performed with the module 
[PersistenceDiagramClustering](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagramClustering.html)
(line 32).

For visualization purposes, we will then compute a 2D layout of the ensemble, 
where each ensemble member will be represented by a point and where the 2D 
distance between 2 points will encode the Wasserstein distance between their 
diagrams. This will provide an intuitive planar overview of the ensemble.
For this, we will first compute a matrix of Wasserstein distances 
with the module 
[PersistenceDiagramDistanceMatrix](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagramDistanceMatrix.html)
(line 39). The resulting 
distance matrix is visualized at the bottom of the middle column in the above 
screenshot. There, it can be seen that the Wasserstein distance already 
identifies two major clusters (large blue sub-matrices of low Wasserstein 
distances).
Next (line 67), 
the module 
[DimensionReduction](https://topology-tool-kit.github.io/doc/html/classttkDimensionReduction.html)
is used to compute a 2D layout via 
multidimensional scaling. Finally, the resulting table is turned into a 2D 
point cloud which is ready to be visualized with
[TableToPoints](https://kitware.github.io/paraview-docs/latest/python/paraview.simple.TableToPoints.html)
(line 75). Then, the output is stored to a simple 
CSV file (line 81).

In the above screenshot, the resulting point cloud is shown in the 2 views at  
the bottom right corner of the screenshot. The first view (left) shows the 
point cloud colored by cluster identifier computed by the pipeline. The second 
view (right) show the same point cloud, colored by the ground truth class. 
There, one can directly visualize that the two classifications are identical 
and that, therefore, this topological clustering pipeline succeeded.

For reference, a traditional pipeline based on the L2-distance between the 
"Entrophy" fields is also provided in this example.
For that, the module 
[LDistanceMatrix](https://topology-tool-kit.github.io/doc/html/classttkLDistanceMatrix.html)
is used (line 45) to compute a matrix of the L2 
distances between each scalar field of the ensemble. 
The resulting distance matrix is visualized at the top of the middle column 
in the above screenshot. There, it can be seen that the L2 distance between the 
scalar fields fails at identifying any clear clusters (there are no large blue 
sub-matrices).
Next (line 49), the module 
[DimensionReduction](https://topology-tool-kit.github.io/doc/html/classttkDimensionReduction.html)
is used to compute a 2D layout via 
multidimensional scaling. The resulting table is turned into a 2D point cloud 
with 
[TableToPoints](https://kitware.github.io/paraview-docs/latest/python/paraview.simple.TableToPoints.html)
(line 55). Finally, the k-means algorithm is run on 
this 2D point cloud with the module 
[KMeans](https://kitware.github.io/paraview-docs/latest/python/paraview.simple.KMeans.html).
Then, the output is stored to a simple 
CSV file (line 83).
The resulting clustering can be visualized with the two views at 
the top right corner of the above screenshot. The ground-truth classification 
is provided by the color coding of the points in the second view (right) while 
the classification computed with this traditional pipeline is shown in the 
first view (left). There, it can bee seen that the coloring of the two point 
clouds differ, indicating an incorrect classification by the traditional kMeans 
algorithm. In particular, since all the metadata associated with each ensemble 
member travels down the analysis pipeline, one can select points in these 
planar views to inspect the corresponding datasets and persistence diagrams 
(left two columns of the screenshot). In particular, two members (red and 
yellow spheres) incorrectly marked as belonging to different classes are 
visualized on the left. There, one can see that although the two flows have the 
same "profile" of vortices (number and strengths), these are located in 
drastically different spots of the field, due to the chaotic nature of 
turbulence, hence explaining the reason of failure of traditional 
clustering pipelines.


## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/clusteringKelvinHelmholtzInstabilities.pvsm 
```

## Python code

``` python  linenums="1"
--8<-- "python/clusteringKelvinHelmholtzInstabilities.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/clusteringKelvinHelmholtzInstabilities.py
```


## Inputs
- [khi.cdb](https://github.com/topology-tool-kit/ttk-data/tree/dev/khi.cdb): a 
cinema database containing 32 regular grids describing periodic, 2D Kelvin 
Helmholtz Instabilities (computational fluid dynamics). 
The scalar field of interest is the "Enstrophy" (an established measure of 
vorticity).
The simulation parameters as well as the ground truth classification (two 
classes: beginning or end of the turbulence) are provided as metadata for each 
entry of the database and are carried along the entire pipeline.
See this [publication](https://arxiv.org/abs/2207.14080) for further details.

## Outputs
-  `W2clusteringAndW2dimensionReduction.csv`: 2D point cloud representing the 
input ensemble (1 line = 1 member of the ensemble). The field `ClusterId` 
denotes the class identifier computed with a k-means clustering (with 
k=2) directly performed in the Wasserstein metric space of persistence 
diagrams. *After* that, the 2D layout of the points is computed by 
multidimensional scaling of the matrix of Wasserstein distances between 
persistence diagrams. With this technique, the output classification perfectly 
matches the ground-truth classification.

-  `L2dimensionReductionAndClustering.csv`: 2D point cloud representing the 
input ensemble (1 line = 1 member of the ensemble). The field `ClosestId(0)` 
denotes the class identifier computed with a standard k-means clustering (with 
k=2) obtained *after* a 2D projection of the point cloud. In particular, 
the 2D layout of the points is computed by multidimensional scaling 
of the matrix of L2 distances between the Enstrophy fields. With this 
technique, the output classification does not match the ground-truth 
classification.

## C++/Python API
[CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html)

[CinemaQuery](https://topology-tool-kit.github.io/doc/html/classttkCinemaQuery.html)

[CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html)

[DimensionReduction](https://topology-tool-kit.github.io/doc/html/classttkDimensionReduction.html)

[LDistanceMatrix](https://topology-tool-kit.github.io/doc/html/classttkLDistanceMatrix.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[PersistenceDiagramClustering](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagramClustering.html)

[PersistenceDiagramDistanceMatrix](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagramDistanceMatrix.html)

[ScalarFieldNormalizer](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldNormalizer.html)

[TriangulationManager](https://topology-tool-kit.github.io/doc/html/classttkTriangulationManager.html)
