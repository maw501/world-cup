<h2 align="center">Bayesian modelling of the 2014 world cup</h2>

<div align="center">
  <!--Python version -->
  <a href="https://www.python.org/downloads/release/python-380/">
    <img src="https://https://img.shields.io/badge/python-3.8-blue.svg"
      alt="Python version" />
  </a>
  <!--Commits  -->
  <a href="https://github.com/maw501/world_cup/commits/master">
    <img src="https://img.shields.io/github/last-commit/maw501/world_cup.svg"
      alt="Status version" />
  </a>
</div>
<br />

### Overview
Repository containing Python and Stan code to run [Gelman's](https://statmodeling.stat.columbia.edu/2014/07/13/stan-analyzes-world-cup-data/) simple world cup model from 2014.

**Example of team quality estimated by the Bayesian model:**

![Image](resources/teams.png)

### Getting started

Clone the repository then create the conda environment:

```
git clone https://github.com/maw501/world-cup.git
cd world_cup
conda env create -f environment.yml
```

In order to use the conda environment in a notebook run:

```
python -m ipykernel install --user --name=world_cup
```


### Notebooks

There are two notebooks:

* [`model_overview.ipynb`](https://nbviewer.jupyter.org/github/maw501/world-cup/blob/master/world_cup/notebooks/model_overview.ipynb): a brief explanation of the model. 
* [`fit_model.ipynb`](https://nbviewer.jupyter.org/github/maw501/world-cup/blob/master/world_cup/notebooks/fit_model.ipynb): fits the model on a linear scale per Gelman.
