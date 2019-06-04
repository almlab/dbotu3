Distribution-based OTU calling
==============================

*dbotu3* is a new implementation of Sarah Preheim''s [dbOTU](http://aem.asm.org/content/79/21/6593.long) algorithm.  The scope is narrower, the numerical comparisons are faster, and the interface is more user-friendly.

Read the [documentation](http://dbotu3.readthedocs.io/en/latest/) for:

  - a guide to getting started,
  - an explanation of the algorithm, and
  - the API reference.

You can also read our new [paper](https://doi.org/10.1371/journal.pone.0176335) for more technical details about the algorithm.

The Alm Lab [website](http://almlab.mit.edu/dbotu3.html) also has a short page with information.

For more information on installation, version histories, and how to contribute, please go to the project's [repo](https://github.com/almlab/dbotu3/).

Installation
------------

dbotu3 is on [conda](https://anaconda.org/cduvallet/dbotu) and can be installed as follows:

```
conda install -c cduvallet -c conda-forge dbotu
```

**Note**: the anaconda.org installation instruction (which is missing the `-c conda-forge` part) won't work because conda won't know where to find the [python-levenshtein](https://anaconda.org/conda-forge/python-levenshtein) package.

For [`QIIME 2`](https://qiime2.org/) users, dbotu3 is also available as a [plugin](https://github.com/cduvallet/q2-dbotu).

The [PyPi](https://pypi.python.org/pypi/dbotu) package is no longer updated.

Requirements
------------

- Numpy, SciPy, [BioPython](http://biopython.org), Pandas
- [Levenshtein](https://anaconda.org/conda-forge/python-levenshtein)

Version history
---------------

- 1.5.3: update README to update description on anaconda.org
- 1.5.2: re-organize files so that package is more canonical and plays well with conda
- 1.1 - 1.5: ??
- 1.1: Corrected error where sequence IDs that could be read as integers would not be found in the table
- 1.2: Python 2 compatibility, tox test framework, warnings for improperly-formatted sequence count tables
- 1.2.1: Added setup requirements
- 1.3.0: Improved OTU file header. Split the log file into a debug and progress log.
- 1.4.0: Made an improvement to the Levenshtein-based genetic dissimilarity metric.
- 1.4.1: Account for pandas API change to ``MultiIndex``
- 1.5.0: Added the restart and rep seq scripts
- 1.5.1: New function for Qiime2 compatibility
- 1.5.2: Move files around to make this a Python package (rather than dbotu.py script)
- 1.5.3: Point to conda, rather than PyPi, installation

To-do
-----

- Testing for the restart scripts
- Better coverage for unit tests

Citation
--------

If you use dbOTU3 in a scientific paper, we ask that you cite the
original dbOTU publication (Preheim *et al*.) or the dbOTU3 publication:

Preheim *et al*. Distribution-Based Clustering: Using Ecology To Refine the
Operational Taxonomic Unit. *Appl Environ Microbiol* (2013) doi:10.1128/AEM.00342-13.

Olesen SW, Duvallet C, and Alm EJ. dbOTU3: A new implementation of
distribution-based OTU calling. *PLoS ONE* (2017) doi:10.1371/journal.pone.0176335.

Author
------

If you find a bug or have a request for a new feature, open an issue_.

.. _issue: https://github.com/almlab/dbotu3/issues

Scott Olesen / *swo at alum.mit.edu*
