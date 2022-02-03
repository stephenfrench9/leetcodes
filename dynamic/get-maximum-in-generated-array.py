# https://leetcode.com/problems/get-maximum-in-generated-array/
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0

        arr = [0]*(n+1)
        arr[0] = 0
        arr[1] = 1

        for k in range(2,n+1):
            if k%2 == 0:
                i = int(k/2)
                arr[k] = arr[i]
            else:
                i = int((k - 1)/2)
                arr[k] = arr[i] + arr[i+1]

        return max(arr)

# I missed that the array had to be n+1 large. I wrote at least part of the code assuming that it would be n large. I think I knew that 