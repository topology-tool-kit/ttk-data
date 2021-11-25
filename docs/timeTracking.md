# Time Tracking

![Time tracking screenshot](https://topology-tool-kit.github.io/img/gallery/timeTracking.jpeg)

## Pipeline description


## ParaView

To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
$ paraview states/tribute.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/timeTracking.py"
```

## Inputs

- [timeTracking.vti](https://github.com/topology-tool-kit/ttk-data/raw/dev/timeTracking.vti): vorticity of a 2D vortex street, with time steps as separate data arrays

## Outputs

- `timeTracking.vtp`: polylines of minima and maxima tracked over time

## C++/Python API

[TrackingFromFields](https://topology-tool-kit.github.io/doc/html/classttkTrackingFromFields.html)
