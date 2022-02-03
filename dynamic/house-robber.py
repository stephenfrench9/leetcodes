# https://leetcode.com/problems/house-robber/
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
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