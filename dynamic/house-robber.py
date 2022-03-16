# https://leetcode.com/problems/house-robber/
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        cost_1 = 0
        cost_2 = 0
        cost_3 = 0

        for n in nums:
            cost = n + max(cost_2, cost_3)
            cost_1, cost_2, cost_3 = cost, cost_1, cost_2

        return max(cost_1, cost_2)

    def rob__general_solution(self, nums: List[int]) -> int:
        paths = [(0, -2)] # (score, position)
        for i, n in enumerate(nums):
            for path in paths:
                if path[1] + 1 < i:
                    new_path = (path[0]+n, i)
                    paths.append(new_path)
                    break

            paths.sort(key=lambda x: -x[0])
            paths = paths[:3] # optional (still performant if removed)
            # I am sorting paths on score, not position. It happens to be guarenteed
            # that the most recent 3 positions are the higheset three scorers.
            # it would likely be better to sort on position and then only keep the best three
            # but to max that work, then you would have to choose the maximum ... this is sounding
            # a lot like the solution above. 

        return paths[0][0]

    def rob_fast_but_wierd(self, nums: List[int]) -> int:
        op = 0
        o = 0

        for n in nums:
            o_new = max(o, op+n)
            op_new = o

            o = o_new
            op = op_new

        return max(o, op)


sol=Solution()
print(sol.rob__general_solution([1,2,5,100,1,1,1,3,4,15,25,1,1,2,4]))