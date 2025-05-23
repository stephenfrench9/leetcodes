class Solution:
    def setZeroes(self, matrix: list[list]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        numrows = len(matrix)
        numcols = len(matrix[0])

        for r in range(numrows):
            for c in range(numcols):
                if matrix[r][c] == 0:
                    print(f"({r},{c})")
                    for cc in range(numcols):
                        interest = matrix[r][cc]
                        print(f"({r},{cc}): {interest}")
                        if interest != 0:
                            matrix[r][cc] = "0"
                    for rr in range(numrows):
                        interest = matrix[rr][c]
                        print(f"({rr},{c}): {interest}")
                        if interest != 0:
                            print(f"changing column (r,cc):({rr},{c})")
                            matrix[rr][c] = "0"
                            """Bug: i had the indices as they are in the above loop.
                            I was using a for loop counter variable from an old loop"""

        for r in range(numrows):
            for c in range(numcols):
                matrix[r][c] = int(matrix[r][c])


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
Solution().setZeroes(matrix)
for r in matrix:
    print(r)
