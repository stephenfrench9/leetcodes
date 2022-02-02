# https://leetcode.com/problems/maximum-subarray/submissions/
from typing import List

class Solution:
    # written with indices
    @staticmethod
    def cumulativeArray(nums: List[int]) -> List[int]:
        cumu = [-1]*len(nums)
        cumu[0] = nums[0]
        for i in range(len(nums))[1:]:
            cumu[i] = cumu[i-1] + nums[i]

        return cumu
    # written without indices
    @staticmethod
    def cumulativeArray2(nums: List[int]) -> List[int]:
        cumu = [0]
        for e in nums:
            prev = cumu[-1]
            cumu.append(e+prev)

        return cumu[1:]

    def maxSubArray(self, nums: List[int]) -> int:
        # search the cumulative array for the biggest increase.
        mini = 0
        best = nums[0]
        for ele in self.cumulativeArray2(nums):
           jump = ele - mini
           if jump > best:
               best = jump
           if ele < mini:
               mini = ele

        return best

ob=Solution()
print(ob.maxSubArray(nums=[1,2,3,4,5,6]))
print(ob.maxSubArray(nums=[1]))
print(ob.maxSubArray(nums=[1,1]))
print(ob.maxSubArray(nums=[0,0]))
print(ob.maxSubArray(nums=[-1, -1]))
print(ob.maxSubArray(nums=[20]))


## reflect
# it is hard to explain why I initialized as I did. It is easy to think about and talk about the behavior in the middle of the array, far away from the endpoints.
# I got the initialization value wrong for "mini" at first. My algorithm was otherwise correct.
# We need to search the cumulative array for the biggest jump. Iterate over it, and keep track of the smallest value so far. Then for each element you visit, you can calculate the "best jump". Ok, what is this "smallest value so far" thing? Well, for the first element in the cumulative array, that is effectively 0, right? Because the "jump" at the first element is the size of the first element. I think that makes sense. So it initializes to zero. After the first element, the smallest so far will be correct. If the first element was negative, it will now correctly report as the smallest. If it it is positive, then the smallest so far is still zero, because ... ok getting lost but feeling pretty good ....