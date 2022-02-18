# https://leetcode.com/problems/maximum-length-of-pair-chain/
from typing import List


class Solution:
    # This is wrong, because it assumes the correct answer is a subsequence of the sequence provided.
    # The provided sequence is in practice a set, and they are asking for a sequence as the answer.
    # It is not the case that every possible sequence must be considered, the general strategy here is overkill.
    # Given a chain so far, it is always know which is the next link to choose.
    def findLongestChain_first_attempt(self, pairs: List[List[int]]) -> int:
        bests = []  # (len, far_end)
        bests = sorted(bests, key=lambda x: -x[0])

        for pair in pairs:
            new_best = (1, pair[1])

            for best in bests:
                if pair[0] > best[1]:
                    new_best = (best[0] + 1, pair[1])
                    bests.append(new_best)
                    break

            bests.append(new_best)
            bests = sorted(bests, key=lambda x: -x[0])

    # given remaining links, it can always be known the best next link to choose.
    # This doesn't strike me as a dynamic programming problem.
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        sorted_pairs = sorted(pairs, key=lambda x: -x[1])
        end_of_chain = sorted_pairs.pop()
        length = 1

        while sorted_pairs:
            candidate = sorted_pairs.pop()
            if candidate[0] > end_of_chain[1]:
                length += 1
                end_of_chain = candidate

        return length
