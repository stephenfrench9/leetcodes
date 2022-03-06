# https://leetcode.com/problems/minimum-jumps-to-reach-home/

from typing import List
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        far = max([x]+forbidden)+a+b+1 # From Solutions. I thought it would be x + a*b or something like that.
        jumps = [float('inf')]*(far)
        jumps[0] = 0
        initial = [0]

        while initial:
            jump_to = []

            for k in initial:
                candidates = [k + a, k - b]
                for cand in candidates:
                    if cand not in forbidden and cand > 0 and cand < far and jumps[k] + 1 < jumps[cand]:
                        jumps[cand] = jumps[k] + 1
                        if cand == k + a:
                            jump_to.append(cand)
                        else:
                            second_cand = cand + a
                            if second_cand not in forbidden and second_cand > 0 and second_cand < far and jumps[k] + 2 < jumps[second_cand]:
                                jump_to.append(second_cand)
                                jumps[second_cand] = jumps[k] + 2

            initial = jump_to


        if jumps[x] == float('inf'):
            return -1
        else:
            return jumps[x]


    def minimumJumps__wrong(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        far = x+a*b

        jumps = [float('inf')]*(x+a*b)
        jumps[0] = 0

        initials = [0]

        while initials:
            finals = []
            for i in initials:
                candidates = [i+a, i-b]
                for c in candidates:
                    if c not in forbidden and c > 0 and c < far and jumps[i] + 1 < jumps[c]:
                        jumps[c] = jumps[i] + 1
                        finals.append(c)

            initials = finals

        if jumps[x] == float('inf'):
            return -1
        else:
            return jumps[x]


forbidden = [1,6,2,14,5,17,4]
forbidden = []
a = 16
b = 9
x = 7

aa = Solution()
print(aa.minimumJumps(forbidden, a, b, x))


