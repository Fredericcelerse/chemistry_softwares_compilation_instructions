### Plumed compilation from scratch

You can install the Plumed software following the instructions contained in the Compilation folder. 

### Testing Plumed installation 

To test the Plumed installation, you can launch the following command contained within the test_installation.sh file:
```
plumed driver --plumed plumed.dat --ixyz system.xyz --box 14.6,14.6,14.6 --length-units A
```
