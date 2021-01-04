import pytest

from dynamic_programming import dp_01_knapsack_problem as dp


def naive_recurse(c, vals, wts):
    return dp.Knapsack(c, vals, wts).naive_recurse()
    # return dp.naive_recurse_closure(c, vals, wts)

def test_naive_recurse_exact_fit():
    vals = [5, 5, 5, 5]
    wts = [5, 5, 5, 5]
    assert naive_recurse(20, vals, wts) == 20

    wts = [1, 2, 3, 4]
    assert naive_recurse(10, vals, wts) == 20

def test_naive_recurse_no_fit():
    vals = [5, 5, 5]
    wts = [5, 5, 5]
    assert naive_recurse(3, vals, wts) == 0

def test_naive_recurse_fits_one():
    vals = [4, 4, 4]
    wts = [5, 5, 5]
    assert naive_recurse(5, vals, wts) == 4

def test_naive_recurse_fits_last_element_in_array():
    vals = [4, 5, 6]
    wts = [5, 5, 5]
    assert naive_recurse(5, vals, wts) == 6

def test_naive_recurse_extra_space():
    vals = [5, 5, 5]
    wts = [5, 5, 5]
    assert naive_recurse(20, vals, wts) == 15

def test_naive_recurse_cant_fill():
    vals = [1, 2, 3, 4]
    wts = [10, 5, 3, 2]
    assert naive_recurse(14, vals, wts) == 9

    vals = [10, 3, 2, 1]
    assert naive_recurse(14, vals, wts) == 12
