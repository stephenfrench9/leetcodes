# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        p = 0
        f = 1

        for _ in range(n-1):
            f_new = p + f
            p = f
            f = f_new

        # i = 1
        # while i < n:
        #     f_new = f + p
        #     i += 1
        #     p = f
        #     f = f_new

        return f
