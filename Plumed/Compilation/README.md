# Compilation instructions

## 1/ Download the software and create the conda environment

```
git clone https://github.com/plumed/plumed2.git --branch v2.8 plumed-v2.8
cd plumed-v2.8/
```

```
conda create -n plumed python==3.10.8
```
```
conda activate plumed
conda install -c conda-forge cmake=3.26.1 gcc=8.5.0 gxx=8.5.0 mpi4py mpich
```

> [!CAUTION]
> If the libraries do not work during the compilations, you can load the corresponded modules available on the cluster:
> ```
> module load intel intel-oneapi-mpi intel-oneapi-mkl python gsl fftw
> ```

## 2/ Compile the software 

### MPI compilation:
```
./configure --prefix=/scratch/celerse/plumed-v2.8/ --enable-mpi --enable-modules=all CC=mpicc FC=mpifort CXX=mpic++ --enable-rpath
```

### NO MPI compilation:
```
./configure --prefix=/scratch/celerse/plumed-v2.8/ --enable-modules=all
```
```
make -j 16
```
```
make install
```

> [!CAUTION]
> Each time plumed will be used, enter the command before:
> ```
> export PLUMED_KERNEL=/The/path/to/libplumedKernel.so
> ```
