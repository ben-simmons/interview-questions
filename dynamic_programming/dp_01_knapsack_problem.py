"""
0-1 Knapsack Problem

Given weights and values of n items, put these items in a knapsack of capacity c to get the maximum total value in
the knapsack. In other words, given two integer arrays vals[0..n-1] and wts[0..n-1] which represent values and weights
associated with n items respectively. Also given an integer c which represents knapsack capacity, find out the maximum
value of all subsets of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot
break an item, either pick the complete item, or don’t pick it (0-1 property).
"""


class Knapsack:

    def __init__(self, c, vals, wts):
        self.c = c
        self.vals = vals
        self.wts = wts
        self.n = len(self.vals) - 1

    def naive_recurse(self):
        return self._naive_recurse(self.c, self.n)

    def _naive_recurse(self, c, n):
        """
        Recurse through the entire tree of inclusion combinations and return the combo with highest value that fits in the
        knapsack. Start at the end of array and work backwards.

        @param c: Capacity
        @param n: Current index
        """
        # Base case
        if c == 0:
            result = 0

        elif n == 0:
            result = self.vals[n] if c >= self.wts[n] else 0

        # This element won't fit, so immediately discard it and move on
        elif self.wts[n] > c:
            result = self._naive_recurse(c, n-1)

        # Recurse through the remaining tree of possibilities, where we either include or don't include this element
        else:
            val_yes = self.vals[n] + self._naive_recurse(c-self.wts[n], n-1)
            val_no = self._naive_recurse(c, n-1)
            result = max(val_yes, val_no)

        return result


def naive_recurse_closure(c, vals, wts):
    n = len(vals)-1

    def naive_recurse(c, n):
        # Base case
        if c == 0:
            result = 0

        elif n == 0:
            result = vals[n] if c >= wts[n] else 0

        # This element won't fit, so immediately discard it and move on
        elif wts[n] > c:
            result = naive_recurse(c, n-1)

        # Recurse through the remaining tree of possibilities, where we either include or don't include this element
        else:
            val_yes = vals[n] + naive_recurse(c-wts[n], n-1)
            val_no = naive_recurse(c, n-1)
            result = max(val_yes, val_no)

        return result

    return naive_recurse(c, n)
