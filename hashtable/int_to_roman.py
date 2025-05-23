# https://leetcode.com/problems/integer-to-roman/submissions/1633510911/?envType=problem-list-v2&envId=hash-table


class Solution1:
    def intToRoman(self, num: int) -> str:
        rn = ""

        roman: dict[int, str] = {
            1000: "M",
            500: "D",
            100: "C",
            50: "L",
            10: "X",
            5: "V",
            1: "I",
        }

        rn = ""
        for k in [1000, 100, 10, 1]:
            digit: int
            value: int

            digit = num // k
            value = digit * k
            num -= value

            if digit == 4:
                if value == 400:
                    rn += "CD"
                elif value == 40:
                    rn += "XL"
                elif value == 4:
                    rn += "IV"
            elif digit == 9:
                if value == 900:
                    rn += "CM"
                elif value == 90:
                    rn += "XC"
                elif value == 9:
                    rn += "IX"
            else:
                while value > 0:
                    for chunk in sorted(roman.keys(), reverse=True):
                        if value - chunk >= 0:
                            cha = roman[chunk]
                            rn += cha
                            value -= chunk
                            break

        return rn


class Solution:
    def intToRoman(self, num: int) -> str:
        rn: str
        rn = ""

        thou: int = num // 1000
        for i in range(thou):
            rn += "M"
            num -= 1000

        hun: int = num // 100
        for i in range(hun):
            num -= 100
        if hun == 0:
            pass
        if hun in (1, 2, 3):
            for i in range(hun):
                rn += "C"
        elif hun == 4:
            rn += "CD"
        elif hun == 5:
            rn += "D"
        elif hun in (6, 7, 8):
            rn += "D"
            for i in range(hun - 5):
                rn += "C"
        elif hun == 9:
            rn += "CM"

        ten: int = num // 10
        for i in range(ten):
            num -= 10
        if ten == 0:
            pass
        elif ten in (1, 2, 3):
            for i in range(ten):
                rn += "X"
        elif ten == 4:
            rn += "XL"
        elif ten == 5:
            rn += "L"
        elif ten in (6, 7, 8):
            rn += "L"
            for i in range(ten - 5):
                rn += "X"
        elif ten == 9:
            rn += "XC"
        else:
            raise ValueError()

        if num == 0:
            pass
        if num in (1, 2, 3):
            for i in range(num):
                rn += "I"
        elif num == 4:
            rn += "IV"
        elif num == 5:
            rn += "V"
        elif num in (6, 7, 8):
            rn += "V"
            for i in range(num - 5):
                rn += "I"
        elif num == 9:
            rn += "IX"

        return rn


a = Solution1()
testcase = 58
print(testcase)
print(a.intToRoman(testcase))
