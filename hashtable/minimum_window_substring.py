# https://leetcode.com/problems/minimum-window-substring/?envType=problem-list-v2&envId=hash-table
"""
The incoming state is always two pointers implying a window and a counter on that window. Whether or not this window satisfies gets computed in the loop, because that information must be present in order to decide how to move the pointers. So the evaluation of a window and the establishment of the window actually happen in different iterations, which feels a little bit unusual. This leads to a bit of an unusual stop condition, which can be carried out by the while loop condition, but that then leads to an issue where the pointers are off the end of the string in the body of the loop, because you check the last position and then per normal you update the counters (this is what happened in what should have been the final execution). Thats easy to protect against, but it requires some massaging of the while loop condition and the loop body code. So just have the loop body code exit the moment it needs to, rather than doing some updates and then executing the body again.

python3.10 lets you compare collection.Counters directly! The logic to implement that is not hard, it just needs to use all().

The run time is proportional to the product of the length of the strings.

The space usage is constant in the size of the two input strings, because there are only 26 characters possible, and we are using count dictionaries.

The comparison to decide if it is a valid window got me at first, I made a mistake and said that they had to be equal, but really you can and probably will have some extra characters in the window.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        if not t or not s:
            return s
        trail = 0
        lead = 0
        window = s[trail:lead]
        count = Counter(window)
        ans = Counter(t)
        NO_MIN_WIN: tuple[int, int] = (0, len(s) + 10)
        min_win: tuple[int, int] = NO_MIN_WIN
        # which pointer to move depends on whether or not the
        # count satisfies, and so that must be asked in the loop

        # while lead is not off the end. 0-index of lens(s) is off the string, lead is the first to exclude. And so that means that when lead = len(s), it is still on the string actually. so len(s) + 1.
        while True:
            if all([ans[k] <= count[k] for k in ans.keys()]):
                # starting in python3.10 you can just compare counters with classic comparison operators.
                min_win = min(
                    min_win,
                    (trail, lead),
                    key=lambda x: x[1] - x[0],
                )
                count.update({s[trail]: -1})
                trail += 1
            else:
                if lead == len(s):
                    break
                else:
                    count.update({s[lead]: 1})
                    lead += 1

        if min_win == NO_MIN_WIN:
            return ""
        else:
            return s[min_win[0] : min_win[1]]


s = "ADOBECODEBANC"
t = "ABC"

print(f"s: {s}, t: {t}")
print(Solution().minWindow(s, t))
