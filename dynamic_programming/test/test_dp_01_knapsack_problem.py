import pytest

from dynamic_programming import dp_01_knapsack_problem as dp


def naive_recurse(c, vals, wts):
    return dp.Knapsack(c, vals, wts).naive_recurse()

def naive_recurse_closure(c, vals, wts):
    return dp.naive_recurse_closure(c, vals, wts)


@pytest.mark.parametrize('func', [naive_recurse, naive_recurse_closure])
class TestKnapsack:

    def test_fits_all_exactly(self, func):
        vals = [5, 5, 5, 5]
        wts = [5, 5, 5, 5]
        assert func(20, vals, wts) == 20

        wts = [1, 2, 3, 4]
        assert func(10, vals, wts) == 20

    def test_fits_all_extra_space(self, func):
        vals = [5, 5, 5]
        wts = [5, 5, 5]
        assert func(20, vals, wts) == 15

    def test_fits_one_exactly(self, func):
        vals = [4, 4, 4]
        wts = [5, 5, 5]
        assert func(5, vals, wts) == 4

    def test_fits_none(self, func):
        vals = [5, 5, 5]
        wts = [5, 5, 5]
        assert func(3, vals, wts) == 0

    def test_starts_filling_from_end_of_array(self, func):
        vals = [4, 5, 6]
        wts = [5, 5, 5]
        assert func(5, vals, wts) == 6

    def test_fits_highest_value(self, func):
        vals = [1, 2, 3, 4]
        wts = [10, 5, 3, 2]
        assert func(14, vals, wts) == 9

        vals = [10, 3, 2, 1]
        assert func(14, vals, wts) == 12
