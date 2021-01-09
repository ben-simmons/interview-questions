"""
0-1 Knapsack Problem

Given weights and values of n items, put these items in a knapsack of capacity c to get the maximum total value in
the knapsack. In other words, given two integer arrays vals[0..n-1] and wts[0..n-1] which represent values and weights
associated with n items respectively. Also given an integer c which represents knapsack capacity, find out the maximum
value of all subsets of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot
break an item, either pick the complete item, or don’t pick it (0-1 property).
"""


class ZeroOneKnapsack:

    def __init__(self, c, vals, wts):
        self.c = c
        self.vals = vals
        self.wts = wts
        self.n = len(self.vals) - 1

    def naive_recurse(self):
        return self._naive_recurse(self.c, self.n)

    def _naive_recurse(self, c, n):
        """
        Recurse through the entire tree of inclusion combinations and return the combo with highest value that fits
        in the knapsack. Start at the end of array and work backwards.

        Time complexity: O(2^n). There is potentially a branch in the recursion tree for every binary choice of yes
        (include) or no (don't include).

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
            result = self._naive_recurse(c, n - 1)

        # Recurse through the remaining tree of possibilities, where we either include or don't include this element
        else:
            val_yes = self.vals[n] + self._naive_recurse(c - self.wts[n], n - 1)
            val_no = self._naive_recurse(c, n - 1)
            result = max(val_yes, val_no)

        return result


def naive_recurse(c, vals, wts):
    n = len(vals) - 1

    def _naive_recurse(c, n):
        # Base case
        if c == 0:
            result = 0

        elif n == 0:
            result = vals[n] if c >= wts[n] else 0

        # This element won't fit, so immediately discard it and move on
        elif wts[n] > c:
            result = _naive_recurse(c, n - 1)

        # Recurse through the remaining tree of possibilities, where we either include or don't include this element
        else:
            val_yes = vals[n] + _naive_recurse(c - wts[n], n - 1)
            val_no = _naive_recurse(c, n - 1)
            result = max(val_yes, val_no)

        return result

    return _naive_recurse(c, n)


def dp_recurse(c, vals, wts):
    """
    Optimized version of naive_recurse() using dynamic programming to memoize the results, for better performance
    during recursion. At each level in the recursion tree, even though we don't begin by knowing what the best
    combination of items is, we know that there is only one best combination for remaining capacity c. These solutions
    are the only ones that will get rolled up into higher (lower?) levels of the tree. In other words, even though we
    don't know which subproblems will contribute to the total solution, we can guarantee that the total solution will
    be constructed from the solutions to subproblems.

    Time complexity: O(n*c). The can be at most c distinct best solutions at any level (there's only one way to
    construct the max value from the remaining items), and there are n levels.
    """
    n = len(vals) - 1

    # Store the highest values for remaining c at each level n
    # Use (c+1) and (n+1) for 2D array dimensions to get indexing right
    memo = [[None] * (c + 1) for i in range(n + 1)]

    def _dp_recurse(c, n):
        # Short circuit if we've already found the best possible solution for remaining capacity at this level
        if memo[n][c] is not None:
            return memo[n][c]

        # Base case
        if c == 0:
            result = 0

        elif n == 0:
            result = vals[n] if c >= wts[n] else 0

        # This element won't fit, so immediately discard it and move on
        elif wts[n] > c:
            result = _dp_recurse(c, n - 1)

        # Recurse through the remaining tree of possibilities, where we either include or don't include this element
        else:
            val_yes = vals[n] + _dp_recurse(c - wts[n], n - 1)
            val_no = _dp_recurse(c, n - 1)
            result = max(val_yes, val_no)

        # Once we have plumbed the depths of the recursion tree and have found a solution, add it to the memo
        memo[n][c] = result

        return result

    return _dp_recurse(c, n)
