# Compilation instructions

## 1/ Download the software and create the conda environment

```
git clone --branch release https://github.com/dftbplus/dftbplus.git
cd dftbplus/
```

```
conda create -n deepmd python==3.10.8
```
```
conda activate deepmd
conda install -c conda-forge gcc=8.5.0 gxx=8.5.0 cmake=3.26.1 blas
```
```
pip install tensorflow-cpu==2.8.0 protobuf==3.20.*
```

> [!IMPORTANT]
> For GPU, also install the following libraries:
> ```
> conda install -c conda-forge cuda-toolkit=12.4.1 cudnn=8.9.7.29
> conda install defusco::mvapich2
```
```
> and instead of using tensorflow-cpu, please use:
> pip install tensorflow==2.8.0
> ```

## 2/ Compile the software 

### FOR CPU:
```
cd deepmd-kit && deepmd_source_dir=`pwd`
tensorflow_root=/home/celerse/anaconda3/envs/deepmd/lib/python3.10/site-packages/tensorflow/
pip install .
```
```
cd source/ && mkdir build && cd build/ && deepmd_root=`pwd`
```

```
cmake -DTENSORFLOW_ROOT=$tensorflow_root -DCMAKE_INSTALL_PREFIX=$deepmd_root -DCMAKE_INSTALL_PREFIX=$deepmd_root/source/build/ -DUSE_TF_PYTHON_LIBS=TRUE ..
```

```
make -j4
```
```
make install
```

### FOR GPU:
```
cd deepmd-kit && deepmd_source_dir=`pwd`
tensorflow_root=/home/celerse/anaconda3/envs/deepmd/lib/python3.10/site-packages/tensorflow/
DP_VARIANT=cuda
pip install .
```
```
cd source/ && mkdir build && cd build/ && deepmd_root=`pwd`
```
```
conda env config vars set CUDA_HOME="/home/celerse/anaconda3/envs/deepmd/"
conda env config vars set CUDA_ROOT="/home/celerse/anaconda3/envs/deepmd/"
conda deactivate
conda activate deepmd
```

```
cmake -DTENSORFLOW_ROOT=$tensorflow_root -DCMAKE_INSTALL_PREFIX=$deepmd_root -DUSE_CUDA_TOOLKIT=TRUE -DCUDA_TOOLKIT_ROOT_DIR=$CUDA_HOME -DCMAKE_INSTALL_PREFIX=$deepmd_root/source/build/ -DUSE_TF_PYTHON_LIBS=TRUE ..
```

```
make -j4
```
```
make install
```

[!WARNING]
> Due to conda issues with cuda, you have to change manually several names of cuda libraries:
> ```
> cd /home/celerse/anaconda3/envs/lammps-deepmd-gpu/lib
> ln -s libcudart.so.12 libcudart.so.11.0
> ln -s libcublas.so.12 libcublas.so.11
> ln -s libcublas.so.12 libcublas.so.11.0
> ln -s libcublasLt.so.12 libcublasLt.so.11
> ln -s libcufft.so.11 libcufft.so.10
> ln -s libcusparse.so.12 libcusparse.so.11
> ```
