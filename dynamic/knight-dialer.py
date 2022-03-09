class Solution:
    def knightDialer(self, n: int) -> int:
        n -= 1
        x1, x2, x3, x4, x5, x6, x7, x8, x9, x0 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1

        for ii in range(n):
            x1n = x6 + x8
            x2n = x7 + x9
            x3n = x4 + x8
            x4n = x3 + x9 + x0
            x5n = 0
            x6n = x1 + x7 + x0
            x7n = x2 + x6
            x8n = x1 + x3
            x9n = x2 + x4
            x0n = x4 + x6

            x1, x2, x3, x4, x5, x6, x7, x8, x9, x0 = x1n, x2n, x3n, x4n, x5n, x6n, x7n, x8n, x9n, x0n

        return (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x0) % (
                    10 ** 9 + 7)

    def knightDialer__accepted__but_too_verbose(self, n: int) -> int:
        n -= 1
        counts = [[1] * 3 for i in range(4)]
        counts[3][0] = 0
        counts[3][2] = 0
        delta = [[0] * 3 for i in range(4)]

        transitions = {
            (0, 0): [(1, 2), (2, 1)],
            (0, 1): [(2, 0), (2, 2)],
            (0, 2): [(1, 0), (2, 1)],
            (1, 0): [(0, 2), (2, 0), (3, 1)],
            (1, 1): [],
            (1, 2): [(0, 0), (2, 0), (3, 1)],
            (2, 0): [(1, 2), (0, 1)],
            (2, 1): [(0, 0), (0, 2)],
            (2, 2): [(1, 0), (0, 1)],
            (3, 0): [],
            (3, 1): [(1, 0), (1, 2)],
            (3, 2): [],
        }

        for ii in range(n):
            for k, v in transitions.items():
                delta[k[0]][k[1]] = 0
                for incoming in v:
                    delta[k[0]][k[1]] += counts[incoming[0]][incoming[1]]

            for i, n in enumerate(counts):
                for k, e in enumerate(n):
                    counts[i][k] = delta[i][k]

                    if counts[i][k] > 10 ** 9 + 7:
                        counts[i][k] = counts[i][k] % (10 ** 9 + 7)

        answer = 0
        for i, n in enumerate(counts):
            for k, e in enumerate(n):
                answer += counts[i][k]

            if answer > 10 ** 9 + 7:
                answer = answer % (10 ** 9 + 7)

        return answer


a = Solution()
a.knightDialer(2)
