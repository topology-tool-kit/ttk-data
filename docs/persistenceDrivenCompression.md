# Persistence-Driven Compression

![Persistence-Driven Compression example
Image](https://topology-tool-kit.github.io/img/gallery/persistenceDrivenCompression.jpg)

## Pipeline description

This example helps comparing three outputs of the
[TopologicalCompression](https://topology-tool-kit.github.io/doc/html/classttkTopologicalCompression.html)
filter to the original input grayscale image (top-left view in the above
screenshot), with the following parameters:

- ZFP relative error tolerance set to 50%, no topological compression
  (bottom-left view in the above screenshot),
- Topological loss set to 10%, no ZFP extra compression (top-right view),
- Topological loss set to 10% and ZFP relative error tolerance set to 50% (bottom-right view).

Those files have been generated from the original VTI image using the
[TopologicalCompressionWriter](https://topology-tool-kit.github.io/doc/html/classttkTopologicalCompressionWriter.html)
filter. To read them, Paraview uses its counterpart,
[TopologicalCompressionReader](https://topology-tool-kit.github.io/doc/html/classttkTopologicalCompressionWriter.html).

## ParaView

To reproduce the above screenshot, go to your
[ttk-data](https://github.com/topology-tool-kit/ttk-data) directory
and enter the following command:

``` bash
paraview states/persistenceDrivenCompression.pvsm
```

## Python code

This script loads the uncompressed
[naturalImage_original.vti](https://github.com/topology-tool-kit/ttk-data/raw/dev/naturalImage_original.vti)
input file, saves it as in the TTK Topological Compressed Image Data
file format, using
[TopologicalCompressionWriter](https://topology-tool-kit.github.io/doc/html/classttkTopologicalCompressionWriter.html)
under the hood. The produced file is then loaded with
[TopologicalCompressionReader](https://topology-tool-kit.github.io/doc/html/classttkTopologicalCompressionWriter.html)
and saved back to VTI. This demonstrates the use of the
`TopologicalCompression` I/O modules.

``` python  linenums="1"
--8<-- "python/persistenceDrivenCompression.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/persistenceDrivenCompression.py
```


## Inputs

- [naturalImage_original.vti](https://github.com/topology-tool-kit/ttk-data/raw/dev/naturalImage_original.vti):
  a grayscale picture converted to the VTI format

- [naturalImage_zpf50.ttk](https://github.com/topology-tool-kit/ttk-data/raw/dev/naturalImage_zfp50.ttk):
  the previous image, compressed using `TopologicalCompressionWriter`
  with ZFP compressor only (no topological compression). ZFP relative
  error tolerance was set to 50%.

- [naturalImage_persistence10.ttk](https://github.com/topology-tool-kit/ttk-data/raw/dev/naturalImage_persistence10.ttk):
  the first input image, compressed using
  `TopologicalCompressionWriter` with a Topological loss of 10% and
  without ZFP (ZFP relative error tolerance set to a negative value).

- [naturalImage_persistence10_zpf50.ttk](https://github.com/topology-tool-kit/ttk-data/raw/dev/naturalImage_persistence10_zfp50.ttk):
  the first input image, compressed using
  `TopologicalCompressionWriter` with a Topological loss of 10% and a
  ZFP relative error tolerance set to 50%.

## Outputs

* `uncompressed_naturalImage_persistence10_zfp50.vti`: the first
  input, compressed and saved as a VTI file.

## C++/Python API

[TopologicalCompression](https://topology-tool-kit.github.io/doc/html/classttkTopologicalCompression.html)

[TopologicalCompressionReader](https://topology-tool-kit.github.io/doc/html/classttkTopologicalCompressionWriter.html)

[TopologicalCompressionWriter](https://topology-tool-kit.github.io/doc/html/classttkTopologicalCompressionWriter.html)
