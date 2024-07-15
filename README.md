# EchoPackage README
## Introduction
EchoPackage is a Python package that introduces custom cell magic that allows the contents of a cell to be accumulated and executed within a Jupyter notebook

## Installation
Begin by downloading the EchoPackage folder and then naviagte to the EchoPackage folder

```cd ~/EchoPackage```

While inside the EchoPackage folder, install the package using 

```pip install .```

## Using the cell magic in Juptyer notebook

Before using EchoPackage in your Jupyter Notebook, you need to load it as an extension:

```%load_ext echo_package```

To call the custom magic:

``` %%echo_append ```
followed by any number of print statements, i.e

```
%%echo_append
print('1')
print('12')
```
which should produce an output of:

```
1
12
Success!
```

If you were to create another cell after the previos one with a call to ```%%echo_append``` i.e.
```
%%echo_append
print('123')
print('1234')
```

the state would be preserved such that the previous cells' outputs would be appended together

```
1
12
123
1234
Success!
```



