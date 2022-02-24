# https://leetcode.com/problems/largest-divisible-subset/
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        subs = [[]]

        for n in nums:
            for sub in subs:
                # if you can append n, append it, then break
                if len(sub) == 0 or n % sub[-1] == 0:
                    new_sub = sub.copy()
                    new_sub.append(n)
                    subs.append(new_sub)
                    break

            subs.sort(key=lambda x: -len(x))

        return subs[0]

    def largestDivisibleSubset__heaps(self, nums: List[int]) -> List[int]:
        from heapq import heappop, heappush, heapify

        nums.sort()
        subs = [(0, [])]

        for n in nums:
            next_generation = []
            while subs:
                sub = heappop(subs)
                heappush(next_generation, sub)

                if sub[0] == 0 or n % sub[1][-1] == 0:
                    new_sub_list = sub[1].copy()
                    new_sub_list.append(n)
                    heappush(next_generation, (-len(new_sub_list), new_sub_list))
                    break

            subs += next_generation
            heapify(subs)

        return subs[0][1]

    def largestDivisibleSubset__complicated_but_correct_and_efficient(self, nums: List[int]) -> List[int]:
        result = []
        nums.sort()
        killer = [0]*len(nums)

        for k, initial_divisor in enumerate(nums):
            # new_results = [[3, 15], [3]]
            new_results = [[]]
            new_results[0].append(initial_divisor)
            if killer[k] > 1:
                continue
            else:
                killer[k] = 1

            for i, n in enumerate(nums):
                if i <= k:
                    continue
                legacy_results = []
                for new_result in new_results:
                    divisor = new_result[-1]
                    if n % divisor == 0:
                        if killer[i] > len(new_result) + 1:
                            break
                        else:
                            legacy_result = new_result.copy()
                            legacy_results.append(legacy_result)
                            new_result.append(n)
                            killer[i] = max(len(new_result), killer[i])

                new_results = new_results + legacy_results

            for new_result in new_results:
                if len(new_result) > len(result):
                    result = new_result

        return result

    def largestDivisibleSubset__first_attempt__wrong(self, nums: List[int]) -> List[int]:
        result = []
        nums.sort()

        while nums:
            new_nums = []
            new_result = []
            divisor = nums.pop(0)
            new_result.append(divisor)
            for n in nums:
                if n % divisor == 0:
                    divisor = n
                    new_result.append(n) # ultimately too eager. Should keep new_result unappened too.  
                else:
                    new_nums.append(n) # hard to follow. If this n wasn't selected,
                    # then it can be included in later subsequences. If it was included, then don't offer it as
                    # a possiblity for later subsequences.

            nums = new_nums
            if len(new_result) > len(result):
                result = new_result

        return result

a = Solution()
b = [5,9,18,54,108,540,90,180,360,720]
b.sort()
print(b)
print(a.largestDivisibleSubset([5,9,18,54,108,540,90,180,360,720]))


# [a,2a,2ap,2ab,2abc,2abcd] The problem is that the path jumps into a promising but ultimately
# incorrect path. The easiest fix, to keep both, isn't that easy. It is to start keeping multiple
# results for each starting position.