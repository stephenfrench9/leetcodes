# https://leetcode.com/problems/jump-game-ii/
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        soln = [float('inf')]*len(nums)
        soln[0] = 0
        for i, max_jump in enumerate(nums):
            for jump in range(1, max_jump+1):
                if i+jump > len(nums) - 1:
                    break
                soln[i+jump] = min(soln[i+jump], soln[i] + 1)

        return soln[-1]