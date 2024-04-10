# Instructions for rapidly installing and compiling several chemistry-based softwares
This repository aims at providing insights about compilation and installation instructions on HPC infrastructure for several chemistry-based softwares, which may be often a pain in the neck to install when we are not user-friendly with pure informatics

## Prerequists

### Anaconda
In most of the cases, we will try to install the softwares without having strong dependencies from the cluster libraries. This is mainly due to the fact that, several times, the libraries are updated by the cluster's administrators, leading sometimes to uncompatibilities between our softwares version and the new libraries. 

To avoid such issues as much as possible, it is relevant to create our own conda environment, which allow any user to download their own libraries without requesting the administrator's rights. First, you need to install anaconda, which can be done by downloading the corresponding script (which depend on your cluster architecture) from this website: https://docs.anaconda.com/free/anaconda/install/

In our case, we have a Linux x86_64 machine, we will thus proceed like that: 
1. Click on the link and search the right file
2. Once found, we go through the terminal of our machine and we type:
   ```
   curl -O https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
   ```
3. Install the anaconda environment:
   ```
   bash Anaconda3-2023.09-0-Linux-x86_64.sh
   ```

Then, each time you will need to activate a specific conda environment, you should tap:
```
conda activate name_of_your_env
```
and to exit the conda environment:
```
conda deactivate
```

[!NOTE] Instead of anaconda you can also do the same with miniconda: https://docs.anaconda.com/free/miniconda/index.html

### Modules

## Softwares and libraries

### Plumed

### DFTB+

### LAMMPS

### DeepMD

### QML
