# https://leetcode.com/problems/next-greater-element-i/
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = dict()
        nums2.append(float('inf'))

        stack = [float('inf')]
        for n in nums2:
            while n > stack[-1]:
                # I have found the next greater element.
                resolved = stack.pop()
                if n == float('inf'):
                    greater[resolved] = -1
                else:
                    greater[resolved] = n
            stack.append(n)

        ans = [0]*len(nums1)
        for i, n in enumerate(nums1):
            ans[i] = greater[n]

        return ans


    def nextGreaterElement__naive(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1]*len(nums1)
        for i, n in enumerate(nums1):
            matching_index2 = -1
            for j, m in enumerate(nums2):
                if n == m:
                    matching_index2 = j
                    break

            for k in nums2[matching_index2+1:]:
                if k > n:
                    ans[i] = k
                    break

        return ans