# https://leetcode.com/problems/maximum-product-subarray/
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = -float('inf')
        adj_max = 1
        adj_min = 1

        for v in nums:
            this_max = max(v, adj_max*v, adj_min*v)
            new_result = max(result, this_max)
            new_adj_max = this_max
            new_adj_min = min(v, adj_max*v, adj_min*v)

            result = new_result
            adj_max = new_adj_max
            adj_min = new_adj_min

        return result


    def maxProduct_accepted(self, nums: List[int]) -> int:
        mpp = [0]*len(nums)
        mnn = [0]*len(nums)
        mnn[0] = min(0, nums[0])
        mpp[0] = max(0, nums[0])
        for i, v in enumerate(nums):
            if i == 0:
                continue
            cand1 = mpp[i-1]*nums[i]
            cand2 = mnn[i-1]*nums[i]
            cand3 = nums[i]

            mini = min(cand1, cand2, cand3)
            maxi = max(cand1, cand2, cand3)

            mnn[i] = mini if mini < 0 else 0
            mpp[i] = maxi if maxi > 0 else 0

        maxpos = max(mpp)

        if maxpos > 0:
            return maxpos
        else:
            return max(mnn)

