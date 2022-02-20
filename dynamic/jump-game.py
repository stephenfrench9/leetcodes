# https://leetcode.com/problems/jump-game/

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
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