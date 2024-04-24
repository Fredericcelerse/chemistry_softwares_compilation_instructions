### QML installation from yml files

You can install qml libraries using already provided environments to build more efficiently your deepmd environment.
To deal with the version coming from master in 2022 you just have to type:
```
conda env create -f qml.yml 
```
or if you want to use the dev one (usefull if you need to use FCHL19):
```
conda env create -f qml-dev.yml 
```

Importantly, you need to ensure that specific libraries are available when you will launch your compuations. Here is listed the commands you need to enter in your submission file:

module load gcc/8.4.0

