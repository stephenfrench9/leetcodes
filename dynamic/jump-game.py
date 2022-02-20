# https://leetcode.com/problems/jump-game/

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        for i, v in enumerate(nums):
            if i > max_index:
                return False
            else:
                max_index = max(max_index, i + v)
        return True


    def canJump__too_slow__typical_dynamic_programming(self, nums: List[int]) -> bool:
        soln = [False]*len(nums)
        soln[0] = True

        for i, max_jump in enumerate(nums):
            # soln[i] is either reachable or not
            if soln[i]:
                for jump in range(1, max_jump+1):
                    if i + jump >= len(nums):
                        break
                    soln[i + jump] = True
        return soln[-1]


    def canJump__too_slow__full_tree(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        reachable = {0}

        while reachable:
            index=reachable.pop()
            step=nums[index]
            for k in range(1,step+1):
                new_index=index + k
                if new_index == len(nums) - 1:
                    return True
                if new_index < len(nums) - 1:
                    reachable.add(new_index)
        return False