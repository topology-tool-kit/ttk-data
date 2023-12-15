# Welcome to the TTK Online Example Database!

This website hosts a list of data analysis pipelines exemplifying the usage of [TTK](https://topology-tool-kit.github.io/) with
[ParaView](http://paraview.org) and its Python API `pvpython`.

This website is targeting novice users who are not power users of [ParaView](http://paraview.org) but who would like to get started with topological data analysis with [TTK](https://topology-tool-kit.github.io/) in Python.

Each example includes:

- a screenshot (or a tutorial video)
- a short description
- the command line to reproduce the example with [ParaView](http://paraview.org)
- the corresponding Python code, to:
    - load the input data 
    - execute the analysis pipeline
    - store the output to disk (for later analysis or visualization, e.g. with [ParaView](http://paraview.org))
- a description of the inputs and outputs
- pointers to the corresponding C++/Python documentation

This documentation assumes a default installation of the latest version of TTK (with the `pvpython` API support enabled) and that the repository [ttk-data](https://github.com/topology-tool-kit/ttk-data) has been downloaded locally.

If you have any questions regarding these examples, please let us know by sending an email to the [TTK user mailing list](mailto:ttk-users@googlegroups.com)!

## Scalar data

| Name | Screenshot |
|:-:|:-:|
| [Dragon](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/dragon.jpg) |
| [Morse persistence](morsePersistence/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/morsePersistence.jpg) |
| [Built-in example 1](BuiltInExample1/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/builtinExample1.jpg) |
| [Interaction site](interactionSites/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/interactionSites.jpg) |
| [Morse molecule](morseMolecule/) |![ExampleImage](https://topology-tool-kit.github.io/img/gallery/morseMolecule.jpg) |
| [Morse-Smale segmentation AT](morseSmaleSegmentation_at/) |![ExampleImage](https://topology-tool-kit.github.io/img/gallery/morseSmaleSegmentation_at.jpg) |
| [Tectonic puzzle](tectonicPuzzle/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/geology.jpg) |
| [CT bones](ctBones/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/ctBones.jpg) |
| [Tribute](tribute/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/tribute.jpg) |
| [Image processing](imageProcessing/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/imageProcessing.jpg) |
| [Persistence driven compression](persistenceDrivenCompression/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceDrivenCompression.jpg) |
| [Morse-Smale quadrangulation](morseSmaleQuadrangulation/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/morseSmaleQuadrangulation.jpg) |
| [Persistent Generators Molecule](persistentGenerators_at/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistentGenerators_at.jpg) |
| [Persistent Generators Cosmic Web](persistentGenerators_darkSky/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistentGenerators_darkSky.jpg) |

## Bivariate scalar data

| Name | Screenshot |
|:-:|:-:|
| [Built-in example 2](builtInExample2/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/builtinExample2.jpg) |

## Uncertain scalar data

| Name | Screenshot |
|:-:|:-:|
| [Uncertain starting vortex](uncertainStartingVortex/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/uncertainStartingVortex.jpg) |

## Time-varying scalar data

| Name | Screenshot |
|:-:|:-:|
| [Time tracking](timeTracking/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/timeTracking.jpeg) |
| [Merge tree temporal reduction](mergeTreeTemporalReduction/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/mergeTreeTemporalReduction.jpg) |
| [Nested tracking graph](nestedTrackingFromOverlap/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/nestedTrackingGraph.jpg) |

## Ensemble scalar data

| Name | Screenshot |
|:-:|:-:|
| [Persistence diagram distance](persistenceDiagramDistance/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceDiagramDistance.jpg) |
| [Persistence diagram clustering](persistenceDiagramClustering/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceDiagramClustering.jpg) |
| [Clustering Kelvin Helmoltz Instabilities](clusteringKelvinHelmholtzInstabilities/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/clusteringKelvinHelmholtzInstabilities.jpg) |
| [Merge tree clustering](mergeTreeClustering/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/mergeTreeClustering.jpg) |
| [Merge tree principal geodesic analysis](mergeTreePGA/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/mergeTreePGA.jpg) |
| [Contour tree alignment](contourTreeAlignment/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/contourTreeAlignment.jpg) |
| [Persistent Generators Periodic Picture](persistentGenerators_periodicPicture/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistentGenerators_periodicPicture.jpg) |


## High-dimensional / point cloud data

| Name | Screenshot |
|:-:|:-:|
| [TopoMap Teaser](topoMapTeaser/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/topoMapTeaser.jpg) |
| [Persistent Generators Household Analysis](persistentGenerators_householdAnalysis/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistentGenerators_householdAnalysis.jpg) |
| [Karhunen-Love Digits 64-Dimensions](karhunenLoveDigits64Dimensions/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/karhunenLoveDigits64Dimensions.jpg) |
| [Persistence clustering0](persistenceClustering0/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceClustering0.jpeg) |
| [Persistence clustering1](persistenceClustering1/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceClustering1.jpeg) |
| [Persistence clustering2](persistenceClustering2/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceClustering2.jpeg) |
| [Persistence clustering3](persistenceClustering3/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceClustering3.jpeg) |
| [Persistence clustering4](persistenceClustering4/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceClustering4.jpeg) |
| [Persistence clustering gallery](persistenceClusteringGallery/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceClusteringGallery.jpeg) |
| [1-manifold learning](1manifoldLearning/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/1manifoldLearning.jpeg) |
| [1-manifold learning circles ](1manifoldLearningCircles/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/1manifoldLearningCircles.jpeg) |
| [2-manifold learning](2manifoldLearning/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/2manifoldLearning.jpeg) |


## In-situ features

| Name | Screenshot |
|:-:|:-:|
| [Geometry approximation](geometryApproximation/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/geometryApproximation.jpg) |

## Misc features

| Name | Screenshot |
|:-:|:-:|
| [Persistent Generators Casting](persistentGenerators_casting/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistentGenerators_casting.jpg) |
| [Persistent Generators Fertility](persistentGenerators_fertility/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistentGenerators_fertility.jpg) |
| [Persistent Generators Skull](persistentGenerators_skull/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistentGenerators_skull.jpg) |
| [Manifold checks](manifoldCheck/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/manifoldCheck.jpg) |
| [Cinema IO](cinemaIO/) | <iframe  width="100%" height="420" src="https://www.youtube.com/embed/yKyiRzPbs0U" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> |
| [Compact Triangulation](compactTriangulation/) | <iframe  width="100%" height="420" src="https://www.youtube.com/embed/vDQRh_tuUSA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> |
