# Test Notebook Collection with plenty of plot elements from the great bqplot work

[![Travis](https://travis-ci.org/bloomberg/bqplot.svg?branch=master)](https://travis-ci.org/bloomberg/bqplot)
[![Documentation](https://readthedocs.org/projects/bqplot/badge/?version=latest)](http://bqplot.readthedocs.org)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bloomberg/bqplot/stable?filepath=examples/Index.ipynb)
[![Chat](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/jupyter-widgets/Lobby)

2-D plotting library for Project Jupyter

## Introduction

bqplot is a 2-D visualization system for Jupyter, based on the constructs of
the *Grammar of Graphics*.

## Goals

-   provide a unified framework for 2-D visualizations with a pythonic API.
-   provide a sensible API for adding user interactions (panning, zooming, selection, etc)

Two APIs are provided

- Users can build custom visualizations using the internal object model, which
  is inspired by the constructs of the Grammar of Graphics (figure, marks, axes,
  scales), and enrich their visualization with our Interaction Layer.
- Or they can use the context-based API similar to Matplotlib's pyplot, which
  provides sensible default choices for most parameters.

### Dependencies

This package depends on the following packages:

- `ipywidgets` (version >=7.0.0, <8.0)
- `traitlets` (version >=4.3.0, <5.0)
- `traittypes` (Version >=0.2.1, <0.3)
- `numpy`
- `pandas`

## Documentation (addition)
A few elements to show-case the Sponge City work is added, but ONLY to show-case the ideas

## Documentation (foundation)

To get started with using `bqplot`, check out the full documentation

https://bqplot.readthedocs.io/

## License

This software is licensed under the Apache 2.0 license. See the [LICENSE](LICENSE) file
for details.

