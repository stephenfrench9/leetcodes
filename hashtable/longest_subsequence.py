# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) in (0, 1):
            return len(s)

        pos = {}
        # consider = 1
        first = 0
        last = 0
        sub: str = s[first : last + 1]
        pos[s[0]] = 0
        best = 1

        for consider, ch in enumerate(s):
            if consider == 0:
                continue
            if ch in sub:
                # harvest
                size = last - first + 1
                best = max(size, best)
                first = pos[ch] + 1
            last = consider
            sub = s[first : last + 1]
            pos[ch] = consider

        best = max(last - first + 1, best)
        return best


a = Solution()

testcase = "pwwkewo"
print(testcase)
longestSub: int = a.lengthOfLongestSubstring(testcase)
print(longestSub)

print()

testcase = "abcabcbb"
print(testcase)
longestSub: int = a.lengthOfLongestSubstring("abcabcbb")
print(longestSub)

print()
