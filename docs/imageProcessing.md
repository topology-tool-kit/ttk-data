# Image Processing 

![Image Processing example
Image](https://topology-tool-kit.github.io/img/gallery/imageProcessing.jpg)


## Pipeline description

This example processes a grayscale image (top left view on the
above screenshot) to generate a segmentation. We will construct the
segmentation from the image gradient.

First, the image is loaded from disk. The gradient is computed with
ParaView's `ComputeDerivatives` or `Gradient` filters. Since TTK only
works on scalar field, a `Calculator` is used to compute the gradient
magnitude.

From the gradient magnitude, a simplification step involving
[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)
(bottom left view) and
[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)
helps removing the noise in the gradient (top right view).

To segment the image, we use the
[MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html)
filter. Since in the input image the objects correspond to low values
in the gradient and their edges to high values, we are interested in
the `DescendingManifold` scalar field of the `Segmentation` output, whose
cells represent regions of low scalar field values.

The
[IdentifierRandomizer](https://topology-tool-kit.github.io/doc/html/classttkIdentifierRandomizer.html)
filter is eventually used in order to color neighbor cells with a
distinct color (bottom right view on the above screenshot).

## ParaView

To reproduce the above screenshot, go to your
[ttk-data](https://github.com/topology-tool-kit/ttk-data) directory
and enter the following command:

``` bash
paraview states/imageProcessing.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/imageProcessing.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/imageProcessing.py
```


## Inputs
- [naturalImage.png](https://github.com/topology-tool-kit/ttk-data/raw/dev/naturalImage.png):
  a grayscale PNG picture.

## Outputs
- `Segmentation.vti`: the image segmentation output.


## C++/Python API
[IdentifierRandomizer](https://topology-tool-kit.github.io/doc/html/classttkIdentifierRandomizer.html)

[MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/classttkPersistenceDiagram.html)

[TopologicalSimplification](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplification.html)


