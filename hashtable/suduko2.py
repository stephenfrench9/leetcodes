class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from collections import namedtuple, defaultdict

        Pos = namedtuple("Pos", ["row", "col"])

        def box_number(r, c):
            return r // 3 * 3 + c // 3

        box_positions = defaultdict(list)
        for r in range(9):
            for c in range(9):
                box_positions[box_number(r, c)].append(Pos(r, c))

        def values(positions):
            return [board[pos.row][pos.col] for pos in positions]

        def getpossible(r, c):
            forbidden = [k for k in board[r] if k != "."]

            for i in range(9):
                forbidden += [k for k in board[i][c] if k != "."]
            box_values = values(box_positions[box_number(r, c)])
            forbidden += [k for k in box_values if k != "."]
            allowed = []
            for i in range(1, 10):
                stri = str(i)
                if stri not in forbidden:
                    allowed.append(stri)
            return allowed

        def backtrack(r, c):
            print(r, ", ", c, ": ")
            for i in range(9):
                print(board[i])
            print("\n\n\n")

            if r > 8:
                return True
            if c > 8:
                return backtrack(r + 1, 0)
            if board[r][c] in [str(i) for i in range(1, 10)]:
                return backtrack(r, c + 1)

            options = getpossible(r, c)
            if options:
                for num in options:
                    board[r][c] = num
                    if backtrack(r, c + 1):
                        return True
            board[r][c] = "."
            return False

        backtrack(0, 0)


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

Solution().solveSudoku(board)
