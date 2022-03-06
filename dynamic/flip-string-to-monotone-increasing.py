# https://leetcode.com/problems/flip-string-to-monotone-increasing/
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        solns = [-1]*(len(s)+1)

        number_of_zeros_including_0_element = s.count("0")
        number_of_ones_preceding_0_element = 0

        solns[0] = (number_of_ones_preceding_0_element, number_of_zeros_including_0_element)

        for i, _ in enumerate(solns):
            if i == 0:
                continue
            number_of_preceding_1s = solns[i-1][0]+int(s[i-1])
            number_of_following_0s_inclusive = solns[i-1][1]-(1-int(s[i-1]))

            solns[i] = (number_of_preceding_1s, number_of_following_0s_inclusive)

        solns.sort(key=lambda x: (x[0]+x[1]))

        return solns[0][0] + solns[0][1]
