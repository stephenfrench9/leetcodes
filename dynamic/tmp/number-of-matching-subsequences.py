# https://leetcode.com/problems/number-of-matching-subsequences/
class Solution:
    @staticmethod
    def isSubsequence(s: str, t: str) -> bool:
        # I want to consume the entire substring.
        substring = s
        totalstring = list(t)
        totalstring.reverse()
        for s in substring:
            # s is a character in the substring
            found = False

            while totalstring and not found:
                t = totalstring.pop()
                if s == t:
                    found = True

            if not found:
                return False

        return True

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        return sum([self.isSubsequence(word, s) for word in words])

# first pass was to entirely wrap logic from https://leetcode.com/problems/is-subsequence/ (https://github.com/stephenfrench9/leetcodes/commit/432e7eca5073d4b2741d6625903b5cd45e4a9649)
# too slow.
