from typing import List

# https://leetcode.com/problems/unique-paths-ii/
### The following will run successfully when dropped into the leetcode editor (python3)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # ok here we go.
        # r is the row in the trianle
        # best is the best sum for row it
        r = 0
        best = [i for i in triangle[0]]
        # see, its true

        for r in range(1, len(triangle)):
            # oh no, its not true anymore. best is the best for the prev r
            best = best + [10**4 + 1]
            for c in reversed(range(0, len(best))):
                if c == 0:
                    best[c] = triangle[r][c] + best[c]
                else:
                    best[c] = triangle[r][c] + min(best[c], best[c-1])

        return min(best)


### The previous will run successfully when dropped into the leetcode editor (python3)

# note, I had trouble initializing the array, this article helped:
# https://stackoverflow.com/questions/4056768/how-to-declare-array-of-zeros-in-python-or-an-array-of-a-certain-size

print("it runs")
print(Solution.minimumTotal(Solution, [[2],[3,4],[6,5,7],[4,1,8,3]]))
print(Solution.minimumTotal(Solution, [[0]]))
print(Solution.minimumTotal(Solution, [[1]]))
