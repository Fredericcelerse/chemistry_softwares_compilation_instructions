# Compilation instructions

## 1/ Download the software and create the conda environment

```
git clone --branch release https://github.com/dftbplus/dftbplus.git
cd dftbplus/
```

```
conda create -n dftb+ python=3.10.8
```
```
conda activate dftb+
conda install -c conda-forge gcc=8.5.0 gxx=8.5.0 cmake=3.26.1 blas 
```

> [!CAUTION]
> If the libraries do not work during the compilations, you can load the corresponded modules available on the cluster:
> ```
> module load gcc openblas fftw intel-mkl cmake
> ```

## 2/ Compile the software 

### To enable modules such as D3 corrections or sockets, you can use the follwoing lines:
$ sed -i 's/WITH_SDFTD3 "Whether the s-dftd3 library should be included" FALSE/WITH_SDFTD3 "Whether the s-dftd3 library should be included" TRUE/g' config.cmake
$ sed -i 's/WITH_SOCKETS "Whether socket communication should be allowed for" FALSE/WITH_SOCKETS "Whether socket communication should be allowed for" TRUE/g' config.cmake
> [!NOTE]
> You can also directly change FALSE to TRUE in the config.cmake file by yourself !

### To compile the software, let us do:
```
$ FC=gfortran CC=gcc cmake -DCMAKE_INSTALL_PREFIX=opt/dftb+ -B _build
```
```
$ cmake --build _build -- -j 16
```
```
$ cmake --install _build
```

> [!CAUTION]
> Adjust the path of the "Prefix = ./dftb-3ob-3-1_files/" command in the dftb_in.hsd according to the path of the dftb-3ob-3-1_files/ folder in your machine !
