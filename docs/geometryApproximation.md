# Geometry Approximation example

![Geometry Approximation Example Image](https://topology-tool-kit.github.io/img/gallery/geometryApproximation.jpg)

## Pipeline description
This example loads two geometric structures: the streamlines of a section of ground water and its surrounding stone.

A fake shadow is put on the stone mesh to give the mesh depth values. The stone object is placed within a sphere using [IcosphereFromObject](https://topology-tool-kit.github.io/doc/html/classttkIcosphereFromObject.html). The object and the icosphere is then given to the [CinemaImaging](https://topology-tool-kit.github.io/doc/html/classttkCinemaImaging.html) filter. It generates multiple images of the stone object, and the images are taken from cameras placed on the vertices of the icosphere.

 An approximation of the geometry is calculated from the images using [DepthImageBasedGeometryApproximation](https://topology-tool-kit.github.io/doc/html/classttkDepthImageBasedGeometryApproximation.html). The approximated geometry can be extracted using the Threshold filter.

Giving the icosphere around the object to [IcospheresFromPoints](https://topology-tool-kit.github.io/doc/html/classttkIcospheresFromPoints.html) yields icospheres at the coordinates of the cameras.


## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
$ paraview states/geometryApproximation.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/geometryApproximation.py"
```

## Inputs
- [streamlines.vtp](https://github.com/topology-tool-kit/ttk-data/tree/dev/GroundWater.cdb/streamlines.vtp): a mesh of the streamlines of the ground water.
- [stone.vtp](https://github.com/topology-tool-kit/ttk-data/tree/dev/GroundWater.cdb/stone.vtp): a mesh of the stone around the ground water.

## Outputs
- `CameraNodes.vtp`: the points representing the positions of the cameras used to take images of the geometry.
- `CinemaImages.vtm`: the images from the cameras given in a multiblock.
- `GeometryApproximatedStone.vtm`: the reconstructed objected as a multiblock of meshes.

## C++/Python API
[IcosphereFromObject](https://topology-tool-kit.github.io/doc/html/classttkIcosphereFromObject.html)

[CinemaImaging](https://topology-tool-kit.github.io/doc/html/classttkCinemaImaging.html)

[DepthImageBasedGeometryApproximation](https://topology-tool-kit.github.io/doc/html/classttkDepthImageBasedGeometryApproximation.html)

[IcospheresFromPoints](https://topology-tool-kit.github.io/doc/html/classttkIcospheresFromPoints.html)