# https://leetcode.com/problems/is-subsequence/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
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

# abc, ajjbjjjjc - incorrect answer. I can't see why.
# answer: totalstring.reverse() -> I had wondered about that before but thought that I saw that the pop method returned someething from the front of the array. it must have been the case that my array had something on the  front and the back.
# This was difficult to write for some reason. I felt like I had these two loops, and I was losing track of what could be true at the different points in the loop. What does this block of code do? What can it result in? Those had too many cases. My first strategies lacked overall structure. It seems ok now - vist every character in the substring, at the start of the loop, it hasn't been found in the totalstring. write some code that tries to find it (and also has this side effect of modifying the totalstring), if you can't find it, then its all over. If you did, move onto the next character. If it is the case that you have consumed the totalstring, then one of the searches will just fail, you never have to explicityly say, hey, we ate the whole totalstring, and there is still substring, so return false. It just beecomes really hard to find characters in the totalstring, given that the totalstring is empty.
