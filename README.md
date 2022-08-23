# python-M1TAL

Resources for Master TAL (NLP), first degree, at Inalco.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Alex-bzh/python-M1TAL/main)

## Installation – for those who like not to ask too many questions

1. Download Miniconda, a small version of Anaconda with conda, Python, and some useful packages:  
https://docs.conda.io/en/latest/miniconda.html

2. Get a clone of this repository:

```
$ git clone git@github.com:Alex-bzh/python-M1TAL.git
$ cd python-M1TAL
```

3. Run JupyterLab in its own environment:

```
$ conda env create -f environment.yml
$ conda activate tal-ml
$ jupyter-lab
```

## Installation – for those who want to have fine control over what they install

### Python 3 installation

1. First, check that Python is installed:

```
$ which python
```

If not, donwload the latest version:
https://www.python.org/downloads/

2. Check the version of your Python distribution (at least 3.7):

```
$ python -V
```

If your version is older than 3.7, you may have a specific `python3.7` binary:

```
$ which python3.7
```

If so, note the path and link it with the `python` command:

```
$ ln -s PYTHON3.7_PATH python
```

3. Be sure to have the latest version of `pip`, the Python package manager:

```
$ python -m pip install --user --upgrade pip
```

### Installing a virtual environment

1. As `venv` is already included in the Python standard library, you just need to install a new virtual environment:

```
$ python -m venv tal-ml
```

2. Activate your environment:

```
$ source tal-ml/bin/activate
```

To leave you environment, just run the command `deactivate`.

### Dependencies installation

With `pip`, install all the requested packages into your environment:

```
$ python -m pip install -r requirements.txt
```

### Run JupyterLab

Simply run JupyterLab with a clone of this repository:

```
$ git clone git@github.com:Alex-bzh/python-M1TAL.git
$ cd python-M1TAL
$ jupyter-lab
```
