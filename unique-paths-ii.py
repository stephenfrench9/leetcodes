from typing import List


### The following will run successfully when dropped into the leetcode editor (python3)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        og = obstacleGrid
        rows = len(og)
        cols = len(og[1])

        ans_grid = [[0 for c in range(cols)] for r in range(rows)]
        ans_grid[0] = rows * [1]
        for r in ans_grid:
            r[0] = 1

        print(ans_grid)


### The previous will run successfully when dropped into the leetcode editor (python3)

# note, I had trouble initializing the array, this article helped:
# https://stackoverflow.com/questions/4056768/how-to-declare-array-of-zeros-in-python-or-an-array-of-a-certain-size

print("it runs")
Solution.uniquePathsWithObstacles(Solution, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
