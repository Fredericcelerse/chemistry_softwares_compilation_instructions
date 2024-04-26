# General comments

## DFTB+ compilation from scratch

You can install the DFTB+ software following the instructions contained in the Compilation folder. 

## Testing DFTB+ installation 

To test the dftb= installation, you can launch the following command contained within the test_installation.sh file:
```
export OMP_NUM_THREADS=1
dftb+ dftb_in.hsd
```

> [!CAUTION]
> Adjust the path of the "Prefix = ./dftb-3ob-3-1_files/" command in the dftb_in.hsd according to the path of the dftb-3ob-3-1_files/ folder in your machine !
