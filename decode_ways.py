from typing import List

# https://leetcode.com/problems/unique-paths-ii/
### The following will run successfully when dropped into the leetcode editor (python3)
class Solution:

    def isValid(self, ss: str):
        ss = [int(ss[0]) for s in ss]
        print(ss[0] == 2)
        print((ss[0] == 2 and 1 <= ss[1] <= 6))
        if (ss[0] == 1 | (ss[0] == 2 and 1 <= ss[1] <= 6)):
            return True
        else:
            return False

    def numDecodings(self, s: str) -> int:
        cur = 1
        parsings_prev = 1
        print("s[cur]: ", s[:cur+1])
        if self.isValid(self, ss=s[:cur+1]):
            parsings_cur = 2
        else:
            parsings_cur = 1

        print("prev: " , parsings_prev)
        print("cur :", parsings_cur)
        print(s[:2])
        return self.isValid(self, ss="22")


### The previous will run successfully when dropped into the leetcode editor (python3)

# note, I had trouble initializing the array, this article helped:
# https://stackoverflow.com/questions/4056768/how-to-declare-array-of-zeros-in-python-or-an-array-of-a-certain-size

print("it runs")
print(Solution.numDecodings(Solution, "22"))

