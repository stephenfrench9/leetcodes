# https://leetcode.com/problems/n-th-tribonacci-number/
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        # n > 2
        pp = 0
        p = 1
        t = 1
        i = 2

        # want i = n, 2 + (n-2) = n

        for _ in range(n-2):
            t_new = pp + p + t
            p_new = t
            pp_new = p

            t = t_new
            p = p_new
            pp = pp_new

        return t






