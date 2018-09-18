## About this example

This program shows the attributes of the GPU.

## Requirements

You must have Python and PIP installed in your system. PyCUDA can be installed through PIP:

```bash
$ pip install pycuda
```

If you have problems trying to install pycuda, check out [this post](https://wiki.tiker.net/PyCuda/Installation).

## Run

Open a terminal and type:

```bash
> sh run.sh
```

## Output
A typical output should look like this one.

SIZE = N : MATRIX = N * N
error = max difference gpu vs cpu result


```
1 device(s) found.
Device #0: GeForce GTX TITAN X
  Compute Capability: 5.2
  Total Memory: 12502720 KB
  ASYNC_ENGINE_COUNT: 2
  CAN_MAP_HOST_MEMORY: 1
  CLOCK_RATE: 1076000
  COMPUTE_CAPABILITY_MAJOR: 5
  COMPUTE_CAPABILITY_MINOR: 2
  COMPUTE_MODE: DEFAULT
  CONCURRENT_KERNELS: 1
  ECC_ENABLED: 0
  GLOBAL_L1_CACHE_SUPPORTED: 1
  GLOBAL_MEMORY_BUS_WIDTH: 384
  GPU_OVERLAP: 1
  INTEGRATED: 0
  KERNEL_EXEC_TIMEOUT: 1
  L2_CACHE_SIZE: 3145728
  LOCAL_L1_CACHE_SUPPORTED: 1
  MANAGED_MEMORY: 1
  MAXIMUM_SURFACE1D_LAYERED_LAYERS: 2048
  MAXIMUM_SURFACE1D_LAYERED_WIDTH: 16384
  MAXIMUM_SURFACE1D_WIDTH: 16384
  MAXIMUM_SURFACE2D_HEIGHT: 65536
  MAXIMUM_SURFACE2D_LAYERED_HEIGHT: 16384
  MAXIMUM_SURFACE2D_LAYERED_LAYERS: 2048
  MAXIMUM_SURFACE2D_LAYERED_WIDTH: 16384
  MAXIMUM_SURFACE2D_WIDTH: 65536
  MAXIMUM_SURFACE3D_DEPTH: 4096
  MAXIMUM_SURFACE3D_HEIGHT: 4096
  MAXIMUM_SURFACE3D_WIDTH: 4096
  MAXIMUM_SURFACECUBEMAP_LAYERED_LAYERS: 2046
  MAXIMUM_SURFACECUBEMAP_LAYERED_WIDTH: 16384
  MAXIMUM_SURFACECUBEMAP_WIDTH: 16384
  MAXIMUM_TEXTURE1D_LAYERED_LAYERS: 2048
  MAXIMUM_TEXTURE1D_LAYERED_WIDTH: 16384
  MAXIMUM_TEXTURE1D_LINEAR_WIDTH: 134217728
  MAXIMUM_TEXTURE1D_MIPMAPPED_WIDTH: 16384
  MAXIMUM_TEXTURE1D_WIDTH: 65536
  MAXIMUM_TEXTURE2D_ARRAY_HEIGHT: 16384
  MAXIMUM_TEXTURE2D_ARRAY_NUMSLICES: 2048
  MAXIMUM_TEXTURE2D_ARRAY_WIDTH: 16384
  MAXIMUM_TEXTURE2D_GATHER_HEIGHT: 16384
  MAXIMUM_TEXTURE2D_GATHER_WIDTH: 16384
  MAXIMUM_TEXTURE2D_HEIGHT: 65536
  MAXIMUM_TEXTURE2D_LINEAR_HEIGHT: 65536
  MAXIMUM_TEXTURE2D_LINEAR_PITCH: 1048544
  MAXIMUM_TEXTURE2D_LINEAR_WIDTH: 65536
  MAXIMUM_TEXTURE2D_MIPMAPPED_HEIGHT: 16384
  MAXIMUM_TEXTURE2D_MIPMAPPED_WIDTH: 16384
  MAXIMUM_TEXTURE2D_WIDTH: 65536
  MAXIMUM_TEXTURE3D_DEPTH: 4096
  MAXIMUM_TEXTURE3D_DEPTH_ALTERNATE: 16384
  MAXIMUM_TEXTURE3D_HEIGHT: 4096
  MAXIMUM_TEXTURE3D_HEIGHT_ALTERNATE: 2048
  MAXIMUM_TEXTURE3D_WIDTH: 4096
  MAXIMUM_TEXTURE3D_WIDTH_ALTERNATE: 2048
  MAXIMUM_TEXTURECUBEMAP_LAYERED_LAYERS: 2046
  MAXIMUM_TEXTURECUBEMAP_LAYERED_WIDTH: 16384
  MAXIMUM_TEXTURECUBEMAP_WIDTH: 16384
  MAX_BLOCK_DIM_X: 1024
  MAX_BLOCK_DIM_Y: 1024
  MAX_BLOCK_DIM_Z: 64
  MAX_GRID_DIM_X: 2147483647
  MAX_GRID_DIM_Y: 65535
  MAX_GRID_DIM_Z: 65535
  MAX_PITCH: 2147483647
  MAX_REGISTERS_PER_BLOCK: 65536
  MAX_REGISTERS_PER_MULTIPROCESSOR: 65536
  MAX_SHARED_MEMORY_PER_BLOCK: 49152
  MAX_SHARED_MEMORY_PER_MULTIPROCESSOR: 98304
  MAX_THREADS_PER_BLOCK: 1024
  MAX_THREADS_PER_MULTIPROCESSOR: 2048
  MEMORY_CLOCK_RATE: 3505000
  MULTIPROCESSOR_COUNT: 24
  MULTI_GPU_BOARD: 0
  MULTI_GPU_BOARD_GROUP_ID: 0
  PCI_BUS_ID: 1
  PCI_DEVICE_ID: 0
  PCI_DOMAIN_ID: 0
  STREAM_PRIORITIES_SUPPORTED: 1
  SURFACE_ALIGNMENT: 512
  TCC_DRIVER: 0
  TEXTURE_ALIGNMENT: 512
  TEXTURE_PITCH_ALIGNMENT: 32
  TOTAL_CONSTANT_MEMORY: 65536
  UNIFIED_ADDRESSING: 1
  WARP_SIZE: 32

```

## Extra Resources

 * [PyCuda Examples](https://wiki.tiker.net/PyCuda/Examples/DumpProperties).
 * [NVIDIA toolkit documentation](https://developer.nvidia.com/cuda-toolkit).