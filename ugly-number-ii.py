# https://leetcode.com/problems/ugly-number-ii/
from heapq import heapify, heappush, heappop

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i = 1
        ugly = 1
        candidates = []
        heapify(candidates)
        heappush(candidates, ugly*2)
        heappush(candidates, ugly*3)
        heappush(candidates, ugly*5)

        while i != n:
            next_ugly = heappop(candidates)
            if next_ugly != ugly:
                # add list
                i += 1
                ugly = next_ugly
                # update candidates
                heappush(candidates, ugly*2)
                heappush(candidates, ugly*3)
                heappush(candidates, ugly*5)

        return ugly

print(Solution.nthUglyNumber(Solution, 40))
print("1st ugly number is 1: ", Solution.nthUglyNumber(Solution, 1))
print("2nd ugly is 2: ", Solution.nthUglyNumber(Solution, 2))
print("3rd ugly is 3: ", Solution.nthUglyNumber(Solution, 3))


