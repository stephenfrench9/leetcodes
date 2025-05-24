# https://leetcode.com/problems/minimum-window-substring/?envType=problem-list-v2&envId=hash-table


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return s

    

        return ''

s = "ADOBECODEBANC"
t = "ABC"

print(f"s: {s}, t: {t}")
print(Solution().minWindow(s, t))
