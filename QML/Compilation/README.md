# Compilation instructions

## 1/ Download the software and create the conda environment

```
git clone -b develop https://github.com/qmlcode/qml
cd qml/
```

```
conda create -n qml python=3.7.4
```
```
conda activate qml
conda install -c conda-forge gcc gxx lapack blas libxcrypt libffi=3.2.1
pip install scipy==1.4.1 ase==3.22.0 scikit-learn
cp /home/celerse/anaconda3/envs/qml/include/crypt.h /home/celerse/anaconda3/envs/qml/include/python3.7m/
export CPATH=/home/celerse/anaconda3/envs/qml/lib/
```

> [!CAUTION]
> scipy 1.4.1 is mandatory for qml, another version can lead to crash ...
> If libraries do not work, you can load your own modules available on the cluster:
> ```
> module load intel intel-oneapi-mkl
> ```

## 2/ Compile the software 

```
LDFLAGS="-L/home/celerse/anaconda3/envs/qml/lib" python setup.py build install
```
> [!NOTE]
> If MKL and intel compilers are available, then you can modify the previous line:
> ```
> LDFLAGS="-L${MKLROOT}/lib/intel64" python setup.py build --compiler=intelem --fcompiler=intelem install
> ```

