# https://leetcode.com/problems/minimum-window-substring/?envType=problem-list-v2&envId=hash-table


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return s

        from collections import Counter

        ans = Counter(t)
        left = 0
        right = 0
        interest = s[left:right]  # ''
        count = Counter(interest)
        ## satisfy? I don't know technically
        ## the state has NOT been considered
        ## when left is pointing at the last element, We still need to consider it, but that is the last time.
        ## when left is off the end of the string, there is nothing more to consider.
        ## when left = len(s)
        best_pair = (0, len(s) + 1)

        while right != len(s) + 1:
            print(f"current window: {left}, {right}")
            print(count)
            print(ans)
            print(ans <= count)
            print()
            print()
            # consider the current window.
            # I have the count for it.
            if ans <= count:
                new_pair = left, right
                best_pair = min(best_pair, new_pair, key=lambda x: x[1] - x[0])
                count.update({s[left]: -1})
                left += 1
            else:
                if right <= len(s) - 1:
                    count.update({s[right]: +1})
                right += 1
            # I now have a window and a count that has not been considered
            # when left is still on the string, I must enter the loop and consider it
            # when left is off the string, I must not enter the loop and consider it.
            # the last 0 index on the string is len(s) - 1.

            # see if the old count satisfies and record it
            # if the new count satisfies, then move the left pointer forward
            ## since it has to satisfy to move left, left will never exceed
            # if the new count does not satisfy, then move the right pointer

        if best_pair == (0, len(s) + 1):
            return ""
        else:
            return s[best_pair[0] : best_pair[1]]


s = "ADOBECODEBANC"
t = "ABC"

print(f"s: {s}, t: {t}")
print(Solution().minWindow(s, t))
