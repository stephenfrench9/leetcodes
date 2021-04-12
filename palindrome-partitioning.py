# https://leetcode.com/problems/palindrome-partitioning/

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        answer = []

        def is_drome(st):
            return st == st[::-1]

        def chew(parsing, cand, rst):

            if rst == "":
                if is_drome(cand):
                    parsing.append(cand)
                    answer.append(parsing)

                return 0

            if is_drome(cand):
                found_parsing = parsing + [cand]
                found_cand = rst[0]
                found_rst = rst[1:]
                chew(found_parsing, found_cand, found_rst)

            continue_parsing = parsing
            continue_cand = cand + rst[0]
            continue_rst = rst[1:]
            chew(continue_parsing, continue_cand, continue_rst)

        parsing_init = []
        cand_init = s[0]
        rst_init = s[1:]

        chew(parsing_init, cand_init, rst_init)
        print(answer)
        return answer

# I am about to run this. I think this algorithm will print out all the possible palindrome parsings.
# Why do I think that? I don't know. It probably wont. But I think it will.
# One nice thing: I make the parent recursive function call on some string, and if that string is empty,
# the call
# stack terminates. Before I make a recursive function call again, I trim this control string. So ...
# since it is trimmed by one, I am guaranteed to control the depth of the call stack for this
# recursive, forking strategy I have implemented here. Basically, the recursive function is called
# for each element in the control string (maybe many times), but the depth of the tree, counting the
# parent function call as depth 1, is the length of the string.
# Does that mean it will work? No. It might. It probably means it wont run infinitely long, stuck in some
# endless loop.

# Is this procedure exploring different parsings? Probably.
# Is this procedure exploring the right parsings and making the right decisions? probably.

# try to run, and there are two errors.
# 1) I forgot the return statement in the base case -> I forgot end the call stack after finding a parsing.
# 2) I tried to add a string to an array.

# now it is running.
# behaviour?

case = "s"
print(case)
Solution.partition(Solution, case)
print()
case = "ss"
print(case)
Solution.partition(Solution, case)
print()
case = "sas"
print(case)
Solution.partition(Solution, case)
print()
case = "aaba"
print(case)
Solution.partition(Solution, case)
print()

# Well, behaviour looks right.


