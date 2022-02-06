# https://leetcode.com/problems/maximum-length-of-pair-chain/
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        bests = [] # (len, far_end)
        bests = sorted(bests, key=lambda x: -x[0])

        for pair in pairs:
            new_best = (1, pair[1])

            for best in bests:
                if pair[0] > best[1]:
                    new_best = (best[0]+1, pair[1])
                    bests.append(new_best)
                    break

            bests.append(new_best)
            bests = sorted(bests, key=lambda x: -x[0])
