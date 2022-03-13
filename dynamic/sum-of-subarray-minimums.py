# https://leetcode.com/problems/sum-of-subarray-minimums/
from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # Each subarray 'belongs' to its earliest minimum.
        # ie [1-,2,3,4,1+,7,5] all subs including 1- and 1+ belong to 1-.
        total = 0
        stack = [-1]  # increasing stack
        arr.append(-float('inf'))
        for i, n in enumerate(arr):
            # find all the sub-arrays for which n is the minimum.
            # a subarray <-> prefix + n + suffix.
            # how many prefixes? 1 + number of elements that are larger (null prefix is valid)
            # how many suffixes? 1 + number of elements that are larger (null suffix is valid)
            # contribution = prefixes*suffixes*n
            while arr[i] < arr[stack[-1]]:  # if same, don't pop. You are acking an edge when you pop.
                array_center = stack.pop()
                far_right = i - array_center
                far_left = array_center - stack[-1]
                total += far_right * far_left * arr[array_center]
            stack.append(i)

            # every element gets added to the stack. When it comes off the stack, it increments the total.

        return int(total % (1e9+7))


    def sumSubarrayMins_accepted(self, arr: List[int]) -> int:
        # Each subarray 'belongs' to its earliest minimum.
        # ie [1-,2,3,4,1+,7,5] all subs including 1- and 1+ belong to 1-.
        total = 0
        stack = [-1]  # increasing stack
        arr.append(-float('inf'))
        for i, n in enumerate(arr):
            # find all the subarrays for which n is the minimum.
            # a subarray <-> prefix + n + suffix.
            # how many prefixes? 1 + number of elements that are larger (null prefix is valid)
            # how many suffixes? 1 + number of elements that are larger (null suffix is valid)
            # contribution = prefixes*suffixes*n
            if arr[i] >= arr[stack[-1]]:
                stack.append(i)
            else:
                while arr[i] < arr[stack[-1]]:  # if same, don't pop. You are acking an edge when you pop.
                    array_center = stack.pop()
                    far_right = i - array_center
                    far_left = array_center - stack[-1]
                    total += far_right * far_left * arr[array_center]
                stack.append(i)

            # every element gets added to the stack. When it comes off the stack, it increments the total.

        return total % (1e9+7)

    def sumSubarrayMins_naive(self, arr: List[int]) -> int:
        total = 0
        for i, n in enumerate(arr):
            mini = n
            for j, m in enumerate(arr[i:]):
                # i + j is the index of the final element in the subarray
                mini = min(m, mini)
                total += mini

        return total % (10 ** 9 + 7)


a = Solution()
print("min_sum of 1,2,3 is 10")
print(a.sumSubarrayMins([3,1,2,4]))
