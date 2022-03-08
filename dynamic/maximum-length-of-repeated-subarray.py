# www.leetcode.com/problems/maximum-length-of-repeated-subarray/
from typing import List
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Visit every pair, if they match, ask for the length of the chain ending at the previous pair, increment, and note the length of the chain ending at this pair.

        curr is notes for the current row (current character in the first string)
        prev is notes for the previous row (previos character in the first string)

        So prev has lengths of shared substrings that ended with the previous character in the first substring, and all characters in the second substring. To look at the "previous pair" for a given pair, where the first string character is fixed because we are looking at one row at a time, you need the just the previous row to consider the previous character from the first substring. For the second substring, we are considering all characters within this for loop, so we need the whole row. Thats confusing to say. This is hard to talk about. 
        """
        curr = [0]*(len(nums2)+1)
        longest = 0
        for i, n in enumerate(nums1):
            prev = curr
            curr = [0]*(len(nums2)+1)
            for j, m in enumerate(nums2):
                if n == m:
                    curr[j+1] = prev[j] + 1
            longest = max([longest] + curr)

        return longest

    def findLength__time_limit_exceeded(self, nums1: List[int], nums2: List[int]) -> int:
        longest = 0
        for i, n in enumerate(nums1):
            for j, m in enumerate(nums2):
                if n == m:
                    k = 1
                    while i+k < len(nums1) and j+k < len(nums2) and nums1[i+k] == nums2[j+k]:
                        k += 1
                    longest = max(longest, k)
        return longest

a = Solution()
print(a.findLength([1,2,3,4], [2,3,4]))