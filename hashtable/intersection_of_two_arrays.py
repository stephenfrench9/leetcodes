# https://leetcode.com/problems/intersection-of-two-arrays/submissions/1639217503/?envType=problem-list-v2&envId=hash-table


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))


class Solution1:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = set()
        for k in nums1:
            if k in nums2:
                ans.add(k)
        return list(ans)


"""
The one liner where you convert everything to sets and then calculate an intersection is much faster.
"""
