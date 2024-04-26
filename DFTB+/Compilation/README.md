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

## Testing DFTB+ installation 

To test the dftb= installation, you can launch the following command contained within the test_installation.sh file:
```
export OMP_NUM_THREADS=1
dftb+ dftb_in.hsd
```

> [!CAUTION]
> Adjust the path of the "Prefix = ./dftb-3ob-3-1_files/" command in the dftb_in.hsd according to the path of the dftb-3ob-3-1_files/ folder in your machine !
