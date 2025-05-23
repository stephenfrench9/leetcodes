# https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=problem-list-v2&envId=hash-table


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        letters: dict

        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        words: list[str] = [""]

        for digit in digits:
            newwords = []
            for letter in letters[digit]:
                for word in words:
                    newwords.append(word + letter)
            words = newwords

        if len(words) == 1:
            return []
        return words

        """
        outputs = ['']
        newoutputs = []
        for digit in digits:
            for letter in letters[digit]:
                for output in outputs:
                    newoutput = output + letter
                    newoutputs.append(newoutput)
        outputs = newoutputs

        return outputs
        """
