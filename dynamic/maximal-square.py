# https://leetcode.com/problems/maximal-square/
from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        curr = [0] * (len(matrix[0]) + 1)
        biggest = 0

        for r, _ in enumerate(matrix):
            prev = curr
            curr = [0] * (len(matrix[r]) + 1)
            for c, _ in enumerate(matrix[r]):
                if int(matrix[r][c]) == 0:
                    curr[c+1] = 0
                elif int(matrix[r][c]) == 1:
                    curr[c+1] = min(curr[c], prev[c], prev[c+1])+1
            biggest = max(curr + [biggest])

        return biggest**2


    def maximalSquare__accepted_first_solution(self, matrix: List[List[str]]) -> int:
        soln = []
        for r, _ in enumerate(matrix):
            soln.append([0]*len(matrix[0]))

        biggest = 0
        for i, _ in enumerate(matrix[0]):
            soln[0][i] = int(matrix[0][i])
            biggest = max(biggest, soln[0][i])

        for i, _ in enumerate(matrix):
            soln[i][0] = int(matrix[i][0])
            biggest = max(biggest, soln[i][0])

        for r, _ in enumerate(matrix):
            for c, _ in enumerate(matrix[r]):
                if r == 0 or c == 0:
                    continue
                elif int(matrix[r][c]) == 0:
                    soln[r][c] = 0
                else:
                    soln[r][c] = min(soln[r-1][c-1], soln[r][c-1], soln[r-1][c]) + 1
                    biggest = max(biggest, soln[r][c])

        return biggest**2

matrix = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]

a = Solution()
print(a.maximalSquare(matrix))