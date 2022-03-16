# www.leetcode.com/problems/delete-and-earn/
from typing import List

from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        c = Counter(nums)
        scores = [0]*int(1e4)
        for k in c.keys():
            scores[k-1] = c[k]*k

        b3, b2, b1 = 0, 0, 0

        for n in scores:
            new_best = n + max(b3, b2)
            b3, b2, b1 = b2, b1, new_best

        return max(b1, b2)
