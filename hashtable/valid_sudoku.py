class Solution0:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        from collections import defaultdict

        indices = defaultdict(list)
        for r in range(len(board)):
            for c in range(len(board[0])):
                value = board[r][c]
                if value == ".":
                    continue
                for indice in indices[value]:
                    if r == indice[0]:
                        return False
                    elif c == indice[1]:
                        return False
                    elif (r // 3, c // 3) == (indice[0] // 3, indice[1] // 3):
                        return False
                indices[value].append((r, c))
        return True


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        boxs = [[] for _ in range(9)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                box_i = (r // 3) * 3 + (c // 3)
                value = board[r][c]
                if value == ".":
                    continue
                if value in rows[r] or value in cols[c] or value in boxs[box_i]:
                    return False
                rows[r].append(value)
                cols[c].append(value)
                boxs[box_i].append(value)

        return True


board: list[list[str]] = [
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

print(Solution().isValidSudoku(board))
