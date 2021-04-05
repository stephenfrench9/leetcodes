from collections import defaultdict


class Solution:
    # global counter
    # counter = defaultdict(int)

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        done = [[False for ies in range(0, len(s1)+1)] for ite in range(0, len(s2)+1)]

        # orig_len_s = len(s1)
        # orig_len_t = len(s2)
        # orig_len_x = len(s3)

        def works(s, t, x):
            # tree = str(orig_len_x - len(x)) + '_' + str(orig_len_s - len(s)) + '_' + str(orig_len_t - len(t))
            # counter[tree] += 1
            ies = int(len(s))
            iet = int(len(t))

            # print("***********Exploring***************")
            # print("len(s):", ies)
            # print("len(t):", iet)
            # print("x:", x)
            # print("\n")


            if done[iet][ies]:
                return False
            done[iet][ies] = True

            if len(x) == 0:
                return len(s) == 0 and len(t) == 0

            if len(s) != 0 and s[0] == x[0]:
                if len(t) != 0 and t[0] == x[0]:
                    # s and t
                    return works(s[1:], t, x[1:]) or works(s, t[1:], x[1:])
                else:
                    # s
                    return works(s[1:], t, x[1:])
            else:
                if len(t) != 0 and t[0] == x[0]:
                    # t
                    return works(s, t[1:], x[1:])
                else:
                    # neiter
                    return False

        worksh = works(s1, s2, s3)
        # print(counter)
        return worksh


# print(Solution.isInterleave(Solution, "aa", "bb", "aabb"))
# print(Solution.isInterleave(Solution, "aac", "bb", "aabcb"))
# print(Solution.isInterleave(Solution, "daac", "bb", "aabcbd"))
# print(Solution.isInterleave(Solution, "aa", "bbbbb", "aabb")) #Should be true?
print(Solution.isInterleave(Solution, "aaaaaaaaaaaaaaaa", "aaaaaaaabaaaaaaaa", "aaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaa"))  # Should be true?
print(counter)