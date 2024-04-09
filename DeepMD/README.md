### DeepMD compilation from yml files

You can install deepmd using already provided environments to build more efficiently your deepmd environment.
To do that with CPU you just have to type:
```
conda env create -y deepmd-cpu-environment.yml 
```
or if you want to use GPU
```
conda env create -y deepmd-gpu-environment.yml # FOR GPU
```

Importantly, if you use this way to install deepmd on your linux environment, you need to ensure that specific libraries are available when you will launch your compuations. In the table are listed the commands you need to enter in your submission file:

|CPU|GPU|
|---|---|
|module load intel/2021.6.0 intel-oneapi-mpi/2021.6.0 intel-oneapi-mkl|module load gcc/9.3.0-cuda cuda/11.0.2|
||export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib64|
||export CUDA_VISIBLE_DEVICES="0"|

### DeepMD compilation from source

Instead, if you need to compile DeepMD directly from the source, you can use either the DeepMD-CPU or DeepMD-GPU files. 
