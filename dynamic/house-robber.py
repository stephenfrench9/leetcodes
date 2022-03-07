# https://leetcode.com/problems/house-robber/
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        cost_1 = 0
        cost_2 = 0
        cost_3 = 0

        for n in nums:
            cost = n + max(cost_2, cost_3)
            cost_1, cost_2, cost_3 = cost, cost_1, cost_2

        return max(cost_1, cost_2)

    def rob_fast_but_wierd(self, nums: List[int]) -> int:
        op = 0
        o = 0

        for n in nums:
            o_new = max(o, op+n)
            op_new = o

            o = o_new
            op = op_new

        return max(o, op)


sol=Solution()
print(sol.rob([1,2,5,100]))