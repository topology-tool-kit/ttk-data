# CinemaIO 

<iframe
 width="100%" height="420"
src="https://www.youtube.com/embed/yKyiRzPbs0U"
frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope;
picture-in-picture" allowfullscreen></iframe>

## Pipeline description
This example first loads a cinema database of a simulation from disk, consisting of three dimensional image files, using the [CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html). This outputs a vtkTable.

The database is queried for a selection of images, using [CinemaQuery](https://topology-tool-kit.github.io/doc/html/classttkCinemaQuery.html), which supports SQL queries on `vtkTables` (bottom view shows query result in a spreadsheet view).

Each selected entry in the database is read by the [CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html), which outputs a `vtkMultiBlock` of the images.

The images are sliced with a plane, and each slice is visualized side-by-side using the [GridLayout](https://topology-tool-kit.github.io/doc/html/classttkGridLayout.html) (top view in screenshot).

[ForEach](https://topology-tool-kit.github.io/doc/html/classttkForEach.html) is used to loop through all slices, and then the [ArrayEditor](https://topology-tool-kit.github.io/doc/html/classttkArrayEditor.html) is used to add a FieldData value to each slice. In this case, we add the interval  `SampleInterval` between each queried entry. Each slice is then written to a new cinema database with the [CinemaWriter](https://topology-tool-kit.github.io/doc/html/classttkCinemaWriter.html). Finally, the for-loop is terminated using [EndFor](https://topology-tool-kit.github.io/doc/html/classttkEndFor.html).

## ParaView
To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/cinemaIO.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/cinemaIO.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/cinemaIO.py
```


## Inputs
- [ViscousFingers.cdb](https://github.com/topology-tool-kit/ttk-data/tree/dev/ViscousFingers.cdb): a cinema database of VTK Image files from a simulation.

## Outputs
- `ViscousFingersSampled.cdb`: a cinema database containing the sampled slices of the input cinema database.

## C++/Python API
[ArrayEditor](https://topology-tool-kit.github.io/doc/html/classttkArrayEditor.html)

[CinemaProductReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaProductReader.html)

[CinemaQuery](https://topology-tool-kit.github.io/doc/html/classttkCinemaQuery.html)

[CinemaReader](https://topology-tool-kit.github.io/doc/html/classttkCinemaReader.html)

[CinemaWriter](https://topology-tool-kit.github.io/doc/html/classttkCinemaWriter.html)

[EndFor](https://topology-tool-kit.github.io/doc/html/classttkEndFor.html)

[ForEach](https://topology-tool-kit.github.io/doc/html/classttkForEach.html)

[GridLayout](https://topology-tool-kit.github.io/doc/html/classttkGridLayout.html)



