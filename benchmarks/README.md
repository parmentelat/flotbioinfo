# Purpose

Our goal is to compare the performance of the Needleman & Wunsch algoritme for computing the distance between 2 strings, in C++ *vs* python.

# Files

The most relevant files for this benchmark are :

## python
  * `nw_naive.py` that implements the same algorithm as in the notebook, except that we use `xrange` instead of `range`
  * `nw_rect.py` that computes the actually useful range using min/max function instead of sweeping the whole triangle and then filtering out coordinates that do not fit into the rectangle.

## C++
  * `nw_naive.cxx` that implements the naive algorithm in C++ using `boost`
  * `nw_rect.cxx` with the rectangle computation trick


# Inputs

All runs compute the distance between 2 strings that contain 2000 `A` and 2000 `B` respectively.

# Optimisations

## python
As compared with the notebook, we always use `xrange` which was not possible for the notebook to run smoothly under python3.

Also we run both python codes with [pypy](http://pypy.org/) which in this context turned out to give **really impressive** performance.

## C++
We enable full optimization (see `Makefile`); in particular `-DNDEBUG -DBOOST_UBLAS_NDEBUG` turned out **impressively effective**.

# Requirements

## python
python2.7 and numpy - although the latter is not crucial for the core benchmark

pypy is a useful addition in this context.

## C++
gcc with the `ublas/boost` library and related includes

# `Makefile`

```
make time_nw
```

Will compute a variety of files named `*.time` :

 * The ones ending in `.bin.time` correspond to the C/C++ programs
 * The ones ending in `.pypy.time` correspond to the python code excuted with `pypy`

# Outline
