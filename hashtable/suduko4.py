class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from collections import namedtuple, defaultdict
        from heapq import heappop, heappush

        Pos = namedtuple("Pos", ["row", "col"])

        def box_number(r, c):
            return r // 3 * 3 + c // 3

        row_content = [set() for i in range(9)]
        col_content = [set() for i in range(9)]
        box_content = [set() for i in range(9)]

        for r in range(9):
            for c in range(9):
                interest = board[r][c]
                if interest != ".":
                    row_content[r].add(board[r][c])
                    col_content[c].add(board[r][c])
                    box_content[box_number(r, c)].add(board[r][c])

        order = []

        for r in range(9):
            for c in range(9):
                if board[r][c] in [str(i) for i in range(1, 10)]:
                    continue
                heappush(
                    order,
                    (
                        -len(
                            row_content[r]
                            | col_content[c]
                            | box_content[box_number(r, c)]
                        ),
                        Pos(r, c),
                    ),
                )

        def backtrack():
            for o in order:
                print(f"{o[0]}>{o[1].row},{o[1].col}", end=":")
            print()
            for i in range(9):
                print(board[i])

            if not order:
                return True
            else:
                next_pos = heappop(order)
            spot = next_pos[0]
            r = next_pos[1].row
            c = next_pos[1].col
            print(r, ", ", c, ": ")
            print(row_content[r])
            print(col_content[c])
            print(box_content[box_number(r, c)])
            print(len(row_content[r] | col_content[c] | box_content[box_number(r, c)]))
            print("\n\n\n")
            for num in "123456789":
                if (
                    num not in row_content[r]
                    and num not in col_content[c]
                    and num not in box_content[box_number(r, c)]
                ):
                    board[r][c] = num
                    row_content[r].add(num)
                    col_content[c].add(num)
                    box_content[box_number(r, c)].add(num)
                    if backtrack():
                        return True
                    else:
                        board[r][c] = "."
                        row_content[r].remove(num)
                        col_content[c].remove(num)
                        box_content[box_number(r, c)].remove(num)
            spot = -len(row_content[r] | col_content[c] | box_content[box_number(r, c)])

            heappush(order, (spot, Pos(r, c)))
            return False

        backtrack()


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
