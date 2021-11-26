# CinemaReader example

![Cinema Reader Example Image](https://topology-tool-kit.github.io/img/gallery/cinemaReader.jpeg)

## Pipeline description
This example first loads a cinema database of a simulation from disk, consisting of three dimensional image files, using the [CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html). This outputs a vtkTable.

The database is queried for a selection of images, using [CinemaQuery](https://topology-tool-kit.github.io/doc/html/classttkCinemaQuery.html), which supports SQL queries on vtkTables (bottom view shows query result in a spreadsheet view).

Each selected entry in the database is read by the [CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html), which outputs a vtkMultiBlock of the images.

The images are sliced with a plane, and finally each plane is visualized side-by-side using the [GridLayout](https://topology-tool-kit.github.io/doc/html/classttkGridLayout.html) (top view in screenshot).

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
$ paraview states/cinemaReader.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/cinemaReader.py"
```

## Inputs
- [ViscousFingers.cdb](https://github.com/topology-tool-kit/ttk-data/tree/dev/ViscousFingers.cdb): a cinema database of VTK Image files from a simulation.

## Outputs
- `ViscousFingers.vtm`: the sliced images of the selected entries in the cinema database, in a vtkMultiBlock. 
- `ViscousFingers`: A folder consisting of each image slice. The slices are given as `.vtp` files, which represents meshes.

## C++/Python API
[CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html)

[CinemaQuery](https://topology-tool-kit.github.io/doc/html/classttkCinemaQuery.html)

[CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html)

[GridLayout](https://topology-tool-kit.github.io/doc/html/classttkGridLayout.html)

