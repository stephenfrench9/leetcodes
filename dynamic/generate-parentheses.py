# https://leetcode.com/problems/generate-parentheses/
from functools import reduce
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def per_ele(acc, ele):
            def valid(string1):
                validity_counter = 0
                for c in string1:
                    if c == ')':
                        validity_counter -= 1
                    else:
                        validity_counter += 1
                    if validity_counter < 0:
                        break

                if string1.count('(') <= n and string1.count(')') <= n and validity_counter >= 0:
                    return True
                else:
                    return False

            new_seqs = []
            a = ele + '('
            b = ele + ')'

            if valid(a):
                new_seqs.append(a)
            if valid(b):
                new_seqs.append(b)
            return acc + new_seqs

        seqs = ['']
        grow = True

        while grow:
            longer_sequences = reduce(per_ele, seqs, [])
            grow = len(''.join(longer_sequences)) > len(''.join(seqs))
            if grow:
                seqs = longer_sequences

        return seqs

