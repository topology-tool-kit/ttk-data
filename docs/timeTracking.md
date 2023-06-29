# Time Tracking

![Time tracking screenshot](https://topology-tool-kit.github.io/img/gallery/timeTracking.jpeg)

## Pipeline description

This example loads a 2D time-dependent scalar field, where time steps are stored as a sequence of data arrays.

Using [TrackingFromFields](https://topology-tool-kit.github.io/doc/html/classttkTrackingFromFields.html), a tracking mesh for the temporal evolution of critical points is computed. This filter computes an optimal matching between persistence diagrams (with respect to Wasserstein metric), and discards critical point pairs below a persistence of 1% by default (parameter `Tolerance`).

The state file further contains an animation of the critical points over time.

## ParaView

To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/timeTracking.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/timeTracking.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/timeTracking.py
```


## Inputs

- [timeTracking.vti](https://github.com/topology-tool-kit/ttk-data/raw/dev/timeTracking.vti): time-dependent vorticity of a 2D vortex street, with time steps represented by data arrays '000', '002', ..., '118'

## Outputs

- `timeTracking.vtp`: tracking mesh of critical points

## C++/Python API

[TrackingFromFields](https://topology-tool-kit.github.io/doc/html/classttkTrackingFromFields.html)
