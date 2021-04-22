from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:


        def num_ones(n):
            total = 0
            for i in range(0, 20):
                 total += int(n/2**i) % 2
            return total

        answer = []
        for i in range(0, num+1):
            answer.append(num_ones(i))

        return answer
