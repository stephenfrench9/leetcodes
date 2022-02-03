# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        p=1
        f=2
        i=2

        # want i = n, assume n >= 2
        # 2 + (n-2) = n
        for _ in range(n-2):
            f_new=p+f
            p=f
            f=f_new

        return f