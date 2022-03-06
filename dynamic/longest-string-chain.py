# https://leetcode.com/problems/longest-string-chain/
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))

        def follows(longer: str, shorter: str) -> bool:
            if len(longer) != len(shorter) + 1:
                return False

            found = False
            valid = True
            for i, c in enumerate(shorter):
                if shorter[i] != longer[i]:
                    found = True
                if found:
                    if shorter[i] != longer[i + 1]:
                        valid = False
                else:
                    if shorter[i] != longer[i]:
                        valid = False

            return valid

        chains = []
        for word in words:
            new_chain = []
            for chain in chains:
                if follows(word, chain[-1]):
                    new_chain = chain.copy()
                    break

            new_chain.append(word)
            chains.append(new_chain)
            chains.sort(key=lambda x: -len(x))

        return len(chains[0])


a = Solution()
print(a.longestStrChain(["abc"]))
