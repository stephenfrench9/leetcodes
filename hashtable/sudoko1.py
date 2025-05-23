class Solution:
    def solveSudoku(self, board: list[list[str | list]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from collections import namedtuple
        from collections import defaultdict

        Pos = namedtuple("Pos", ["row", "col"])

        coords: dict[int, list[Pos]] = defaultdict(list)
        for r in range(9):
            for c in range(9):
                box_number = (r // 3) * 3 + c // 3
                coords[box_number].append(Pos(r, c))

        def box_companions(pos: Pos):
            box_number = (pos.row // 3) * 3 + pos.col // 3
            return [
                board[pos.row][pos.col]
                for pos in coords[box_number]
                if board[pos.row][pos.col] != "."
            ]

        # initialize the board
        tracker = {}
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    k: int = r
                    forbidden = []
                    forbidden += [j for j in board[r] if j != "."]
                    for i in range(9):
                        if board[i][c] != ".":
                            forbidden += [board[i][c]]
                    forbidden += box_companions(Pos(r, c))
                    allowed = []
                    for i in range(9):
                        if str(i) not in forbidden:
                            allowed.append(i)
                    board[r][c] = allowed
                    tracker[(r, c)] = (
                        allowed  # tracker is referencing the same list as in board
                    )

        tracker = sorted(
            tracker.items(), key=lambda item: len(item[1]), reverse=True
        )  # tracker is now probably independent

        while tracker:
            discovery = tracker.pop()
            r, c = discovery[0]
            allowed = discovery[1]
            tracker = {}
            print(r)
            print(c)
            print(allowed)
            assert len(allowed) == 1
            board[r][c] = allowed[0]
            for cell in board[r]:
                if isinstance(cell, list):
                    cell.remove(board[r][c])
            for k in range(9):
                for cell in board[k][c]:
                    if isinstance(cell, list):
                        cell.remove(board[r][c])
            for cell in box_companions(r, c):
                if isinstance(cell, list):
                    cell.remove(board[r][c])
            for r in range(9):
                for c in range(9):
                    if isinstance(board[r][c], list):
                        tracker[(r, c)] = board[r][c]
            tracker = sorted(
                tracker.items(), key=lambda item: len(item[1]), reverse=True
            )

        # state is a sorted tracker, and a board.
        # update will be to fill in one square, eliminate that option from other allowed lists, and then rebuild tracker


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
