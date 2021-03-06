# -*- coding: utf-8 -*-

# Parallel Processing Teaching Toolkit
# PyOpenCL - Example 08
# Vector Reduction : Search Minimum
# https://github.com/javierip/parallel-processing-teaching-toolkit

import pyopencl as cl
import numpy as np

import time   # For measure the running times

VECTOR_SIZE = 256 # Elements of vector

# Create a random vector
a_host = np.random.rand(VECTOR_SIZE).astype(np.float32)
# Create a aux vector for GPU operation
b_host = np.zeros(VECTOR_SIZE).astype(np.float32)

# Create a empty vectors for the result
res_host= np.zeros(VECTOR_SIZE).astype(np.float32) # Result in CPU from GPU
result_host= np.zeros(2).astype(np.float32) # Result in CPU

# Create CL context
platform = cl.get_platforms()[0]   
device = platform.get_devices()[0] #get first gpu available

print "Running: ", platform
print "In GPU: ", device

ctx = cl.Context([device])
queue = cl.CommandQueue(ctx)



tic=time.time()

#Operation using the CPU
result_host[0]=100
for i in range(0,VECTOR_SIZE):
    if(a_host[i]<result_host[0]):
        result_host[0]=a_host[i]
        result_host[1]=i

time_cpu=time.time()-tic

print 
print a_host

# Transfer host (CPU) memory to device (GPU) memory 
mf = cl.mem_flags
a_gpu = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a_host)
b_gpu = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b_host)

# Kernel code
prg = cl.Program(ctx, """
__kernel void sum(__global const float *g_idata,  __global float *g_odata) {
  

    __local float sdata[1024];
  	__local  int sindice[1024];


    int tid = get_local_id(0);
    int i = get_global_id(0);
    
    sdata[tid] = g_idata[i];
    sindice[tid] = i;
    
    
 	barrier(CLK_LOCAL_MEM_FENCE);


    for (unsigned int s = get_local_size(0) / 2; s > 0; s >>= 1) {

        if (tid < s ) {
            if (sdata[tid] > sdata[tid + s]) {
                sdata[tid] = sdata[tid + s];
                sindice[tid] = sindice[tid + s];

            }//else sindice[tid] = sindice[tid];
            barrier(CLK_LOCAL_MEM_FENCE);
        }

    }

    if (tid == 0) {
        g_odata[0] = sdata[0];

    }

    if (tid == 1) {
        g_odata[1] = sindice[0];

    }

}
""").build()

# Create empty gpu array for the result 
res_gpu = cl.Buffer(ctx, mf.WRITE_ONLY, a_host.nbytes)


tic=time.time()
#Operation using the GPU - call the kernel on the card
prg.sum(queue, a_host.shape, None, a_gpu,  res_gpu)

time_gpu=time.time()-tic

#Clear GPU resources
res_host = np.empty_like(a_host)
cl.enqueue_copy(queue, res_host, res_gpu)



# Print the results
print "-" * 80
print "Vector Reduction with Vector Size =" , VECTOR_SIZE
print "Min CPU:" , result_host[0]
print "Min GPU:" , res_host[0]
print "Index CPU:" , result_host[1]
print "Index GPU:" , res_host[1]
print "Time CPU:", time_cpu
print "Time GPU:", time_gpu

