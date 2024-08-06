# echo_append README

## Introduction

echo_append is a Python project aimed at creating custom IPython cell magics for Jupyter Notebooks. The primary functionality is to accumulate DOT language code and display the results of all executed cells as PNGs.

## Dependencies

Python 3.11.9
Poetry 1.8.3
Jupyter notebook 7.2.1
IPython 8.26.0
Graphviz 12.0
Pillow 10.4.0

Ensure that you have poetry and jupyter installed

Jupyter installation: https://jupyter.org/install
Poetry installation: https://python-poetry.org/docs/

## Setting up Environment

Begin by cloning the repository from Github and then navigate to the top directory of the project

`cd ~/{location}/{of}/{project}/helical-jupyter`

While inside the `helical-jupyter` folder, create a virtual environment to install the project and its dependencies:

- Windows: `py -m venv {name of your virtual environment}`
- OSX: `python3 -m venv {name of your virtual environment}`

Activate your virtual environment:

Windows: `.\{name of virtual environment}\Sciprts\activate`
OSX:`./{name of virtual environment}/bin/activate`

Install the project (make the package accessible from any location when the virtual environment is activated):

`poetry install`

Launch jupyter notebook and create a new notebook to get started:

`jupyter notebook`

## Using the cell magic in Juptyer notebook

Before using echo_append in your Jupyter Notebook, you need to load it as an extension:

`%load_ext echo_package`

To call the custom magic:

`%%echo_append`
followed by DOT code, i.e

```
%%echo_append
digraph G {
    A -> B;
    B -> C;
    C -> A;
    C -> A;
}
```

which will produce an image of a graph, along with a 'Success!' string appended at the end
(Please see the `Resources` folder for an example image output)

You can enter in some other DOT code in a different cell, which will produce an image as specified in the cell

## Tooling recommendations

Visual Studio Code - IDE for python devlopement
Poetry - dependency management

## Changes to the echo_append script

Modifications to the echo_append script can be made in the `echo_append.py` file in the echo_append directory
