<h2 align="center">Bayesian modelling of the 2014 world cup</h2>

<div align="center">
  <!--Python version -->
  <a href="https://www.python.org/downloads/release/python-360/">
    <img src="https://img.shields.io/pypi/pyversions/fastai.svg"
      alt="Python version" />
  </a>
  <!--Project status -->
  <a href="https://github.com/maw501/world_cup">
    <img src="https://img.shields.io/badge/Status-Under%20development-green.svg"
      alt="Status version" />
  </a>
  <!--Commits  -->
  <a href="https://github.com/maw501/world_cup/commits/master">
    <img src="https://img.shields.io/github/last-commit/maw501/world_cup.svg"
      alt="Status version" />
  </a>
</div>
<br />

Repository containing Python and Stan code to run [Gelman's](https://statmodeling.stat.columbia.edu/2014/07/13/stan-analyzes-world-cup-data/) simple world cup model from 2014.

### Getting started

Aside from standard data science packages the main dependencies are [PyStan](https://pystan.readthedocs.io/en/latest/) and [ArviZ](https://arviz-devs.github.io/arviz/).

### Overview

#### Data

The data consists of the scores for all games from the 2014 world cup up to but excluding the final and 3rd/4th place play-off.

Gelman also uses a version of the [Soccer Power Index](https://projects.fivethirtyeight.com/global-club-soccer-rankings/) for international teams which is just treated in the model as a rank order (not a score).

#### Model


We model the score difference when team $i$ plays team $j$ as $y_{ij}$:

$$y_{ij} \sim \mathcal{t}_{\nu}\, (a_i - a_j, \sigma_y)$$

which is a student-t distribution with $\nu = 7$ degrees of freedom, location $a_i - a_j$ and shared scale $\sigma_y$.

The skill-level parameter $a_i$ of the $i$th team is modelled as:

$$a_i \sim \mathcal{N}(\mu + b \, s_i, \sigma_a)$$

where $s_i$ is the Soccer Power Index for the $i$th team and is used as prior knowledge about the abilities of the teams. This is thus a hierarchical model with each $a_i$ coming from a population level ability distribution. 

However, we care about the *relative* ability of the teams and as $\mu$ is the average of all team's abilities and we are going to compare $a_i$ to $a_j$ for any $i$ and $j$ the $\mu$s will cancel and so we can just set it to 0.

So we instead think of each $a_i$ as the relative ability of a team (relative to the population) and it is modelled as:

$$a_i \sim \mathcal{N}(b \, s_i, \sigma_a)$$

**What do the parameters represent?**

Now we have the model let's quickly explain what the parameters represent:

* $b$: the weight of the prior information in the Soccer Power Index. If this index contains no information we would expect $b$ to be close to 0.
* $\sigma_a$: the residual error in the estimates of team's abilities (as even given the Soccer Power Index we do not expect to be able to estimate ability perfectly).
* $\sigma_y$: the observational residual error - given the relative abilities of the teams we expect errors in our score difference estimates.
* $a_i$: this is the relative ability of each team to the population.


### TODO

* Prior predictive checking
* Posterior predictive checking
* Model checking