# Distributed Persistence Diagram

![DDMS example Image](https://topology-tool-kit.github.io/img/gallery/distributedPersistenceDiagram.jpg)

This toy example illustrates the computation of a persistence diagram in a distributed-memory context with MPI using the Distributed Discrete Morse Sandwich algorithm. For more information on  the usage of TTK in a distributed-memory context, please see the example [MPI example](../mpiExample/).

Please note both ParaView and TTK need to be compiled with MPI (using the CMake flags `PARAVIEW_USE_MPI=ON` and `TTK_ENABLE_MPI=ON` for ParaView and TTK respectively). TTK also requires to be compiled with OpenMP (using the CMake flag `TTK_ENABLE_OPENMP=ON`).
For processing large-scale datasets (typically beyond $1024^3$), we recommend to build TTK with 64 bit identifiers (by setting the CMake flag `TTK_ENABLE_64BIT_IDS=ON`). For performance benchmarks (e.g., for comparing computation times), TTK needs to be built with the advanced CMake option `TTK_ENABLE_MPI_TIME` enabled, in order to display precise computation time evaluations. See the [Performance timing](#performance-timing) section below. 

The execution requires to set a thread support level of `MPI_THREAD_MULTIPLE` at runtime. For the library OpenMPI, this means setting the environment variable `OMPI_MPI_THREAD_LEVEL` to 3 (as shown in the examples below).

## Pipeline description

The produced visualization captures the persistence diagrams of each dimension ($D_0$, $D_1$ and $D_2$, from left to right in the image).

First, the data is loaded and the grid is resampled (to $128^3$ by default). 

Then, a global ordering of the vertices is computed using the filter [ArrayPreconditioning](https://topology-tool-kit.github.io/doc/html/classttkArrayPreconditioning.html). This step will be triggered automatically if not explicitly called.

Finally, the persistence diagram is computed via [PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/PersistenceDiagram_8h.html) and more specifically the algorithm Distributed Discrete Morse Sandwich (specified in the choice of software backend).

## ParaView

To reproduce the above screenshot on 2 processes and 4 threads, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:

``` bash
OMPI_MPI_THREAD_LEVEL=3 OMP_NUM_THREADS=4 mpirun --bind-to none --map-by node -n 2 pvserver 
``` 
In another command line enter the following command:
``` bash
paraview 
```
Now, follow the procedure described in paragraph $8.2.2$ of the following [ParaView documentation](https://docs.paraview.org/en/latest/ReferenceManual/parallelDataVisualization.html#configuring-a-server-connection) to connect your ParaView server to your client. Once that is done, you can open the state file `states/distributedPersistenceDiagram.pvsm` in the ParaView GUI through `File` > `Load State`.

## Python code

``` python  linenums="1"
--8<-- "python/distributedPersistenceDiagram.py"
```

To run the above Python script using 4 threads and 2 processes, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
OMPI_MPI_THREAD_LEVEL=3 OMP_NUM_THREADS=4 mpirun --bind-to none --map-by node -n 2 pvbatch python/distributedPersistenceDiagram.py 
```

By default, the dataset is resampled to $128^3$. To resample to a higher dimension, for example $256^3$, enter the following command:

```bash
OMPI_MPI_THREAD_LEVEL=3 OMP_NUM_THREADS=4 mpirun --bind-to none --map-by node -n 2 pvbatch python/distributedPersistenceDiagram.py 256
```
Be aware that this may require too much memory to execute on a regular laptop.

## Performance timing

To report performance times for the distributed computation of persistence with TTK, replace the string `backpack.vti` in the above Python script with the path to your input VTI file and run the script with `pvpython` as described above. Warning, TTK needs to be built with the advanced CMake option `TTK_ENABLE_MPI_TIME` enabled. Also, please make sure to adjust the number of processes (`-n` option) and threads (`OMP_NUM_THREADS` variable) to your hardware.

In the terminal output, 
the full execution time of the distributed persistence computation (excluding IO) can be obtained by summing the times reported by the three following steps (`4.11599` seconds overall in this example):

- `[ArrayPreconditioning-0] Array preconditioning performed using 2 MPI processes lasted: 0.047390`
- `[DiscreteGradient-0] Computation performed using 2 MPI processes lasted: 2.172824`
- `[DiscreteMorseSandwichMPI-0] Computation of persistence pairs performed using 2 MPI processes lasted: 1.895776`

## Inputs
- [backpack.vti](https://github.com/topology-tool-kit/ttk-data/raw/dev/backpack.vti):  A CT scan of a backpack filled with items.

## Output
- `diagram.pvtu`: the persistence diagram of the backpack dataset.

## C++/Python API

[ArrayPreconditioning](https://topology-tool-kit.github.io/doc/html/classttkArrayPreconditioning.html)

[PersistenceDiagram](https://topology-tool-kit.github.io/doc/html/PersistenceDiagram_8h.html)
