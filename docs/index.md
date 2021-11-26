# Welcome to the TTK Examples!

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

This documentation assumes a default TTK installation (with the `pvpython` API support enabled) and that the repository [ttk-data](https://github.com/topology-tool-kit/ttk-data) has been downloaded locally.

## List of available examples

### Scalar data

| Name | Screenshot |
|:-:|:-:|
| [Dragon example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/dragon.jpg) |
| [Morse persistence example](morsePersistence/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/morsePersistence.jpg) |
| [Built-in example 1](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/builtinExample1.jpg) |
| [Interaction site example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/interactionSites.jpg) |
| [Viscous fingering example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/viscousFingering.jpg) |
| [Morse molecule example](morseMolecule/) |![ExampleImage](https://topology-tool-kit.github.io/img/gallery/morseMolecule.jpg) |
| [Tectonic puzzle example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/geology.jpg) |
| [Ocean vortices example](dragon/) | !![ExampleImage](https://topology-tool-kit.github.io/img/gallery/climate.jpg) |
| [Contour around point example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/contourAroundPoint.jpg) |
| [CT bones example](ctBones/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/ctBones.jpg) |
| [Tribute example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/tribute.jpg) |
| [Image processing example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/imageProcessing.jpg) |
| [Persistence driven compression example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceDrivenCompression.jpg) |
| [Morse-Smale quadrangulation example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/morseSmaleQuadrangulation.jpg) |

### Bivariate scalar data

| Name | Screenshot |
|:-:|:-:|
| [Built-in example 2](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/builtinExample2.jpg) |
| [Bivariate toy example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/bivariateToy.jpg) |
| [Bivariate toy CSP peeling example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/bivariateToyCspPeeling.jpg) |
| [Mechanical example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/mechanical.jpg) |

### Uncertain scalar data

| Name | Screenshot |
|:-:|:-:|
| [Built-in example 3](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/builtinExample3.jpg) |
| [Uncertain starting vortex example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/uncertainStartingVortex.jpg) |

### Time-varying scalar data

| Name | Screenshot |
|:-:|:-:|
| [Time tracking example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/timeTracking.jpeg) |
| [Merge tree feature tracking example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/mergeTreeFeatureTracking.jpg) |
| [Merge tree temporal reduction example](mergeTreeTemporalReduction/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/mergeTreeTemporalReduction.jpg) |
| [Nested tracking graph example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/nestedTrackingGraph.jpg) |

### Ensemble scalar data

| Name | Screenshot |
|:-:|:-:|
| [Persistence diagram distance example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceDiagramDistance.jpg) |
| [Persistence diagram clustering example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceDiagramClustering.jpg) |
| [Merge tree clustering example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/mergeTreeClustering.jpg) |
| [Contour tree alignment example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/contourTreeAlignment.jpg) |

### High-dimensional / point cloud data

| Name | Screenshot |
|:-:|:-:|
| [Persistence clustering gallery example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceClusteringGallery.jpeg) |
| [Persistence clustering0 example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceClustering0.jpeg) |
| [Persistence clustering1 example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceClustering1.jpeg) |
| [Persistence clustering2 example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceClustering2.jpeg) |
| [Persistence clustering3 example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceClustering3.jpeg) |
| [Persistence clustering4 example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceClustering4.jpeg) |
| [Karhunen-Love Digits 64-Dimensions example](karhunenLoveDigits64Dimensions/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/karhunenLoveDigits64Dimensions.jpg) |
| [1-manifold learning example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/1manifoldLearning.jpeg) |
| [1-manifold learning circles  example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/1manifoldLearningCircles.jpeg) |
| [2-manifold learning example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/2manifoldLearning.jpeg) |

### In-situ features

| Name | Screenshot |
|:-:|:-:|
| [Geometry approximation example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/geometryApproximation.jpg) |
| [Cinema darkroom example](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/cinemaDarkroom.jpg) |

### Misc features

| Name | Screenshot |
|:-:|:-:|
| [Manifold checks example](manifoldCheck/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/manifoldCheck.jpg) |

