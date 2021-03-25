from typing import List

# https://leetcode.com/problems/unique-paths-ii/
### The following will run successfully when dropped into the leetcode editor (python3)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        og = obstacleGrid
        rows = len(og)
        cols = len(og[0])

        for row in range(rows):
            for col in range(cols):
                if og[row][col] == 1:
                    og[row][col] = 0
                # og[row][col] must equal zero
                else:
                    if row == 0:
                        if col == 0:
                            og[row][col] = 1
                        else:
                            og[row][col] = og[row][col-1]
                    else:
                        if col == 0:
                            og[row][col] = og[row-1][col]
                        else:
                            og[row][col] = og[row-1][col] + og[row][col-1]

        return og[-1][-1]

### The previous will run successfully when dropped into the leetcode editor (python3)

# note, I had trouble initializing the array, this article helped:
# https://stackoverflow.com/questions/4056768/how-to-declare-array-of-zeros-in-python-or-an-array-of-a-certain-size

print("it runs")
print(Solution.uniquePathsWithObstacles(Solution, [[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(Solution.uniquePathsWithObstacles(Solution, [[0]]))
print(Solution.uniquePathsWithObstacles(Solution, [[1]]))
