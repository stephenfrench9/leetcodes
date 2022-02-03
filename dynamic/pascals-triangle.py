#https://leetcode.com/problems/pascals-triangle/
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        tri = [[1], [1, 1]]

        while len(tri) < numRows:
            next_row = []
            prev = tri[-1][0]
            for v in tri[-1][1:]:
                next_row.append(prev+v)
                prev = v
            next_row.append(1)
            #next_row = [1] + next_row
            next_row.insert(0,1)
            tri.append(next_row)

        return tri

# there is an index error at initialization of prev. I just don't see it at all ....
# what could it be? Well, on the first execution it seems pretty ok ...
# I have tried running the code in my head, I think it is all ok ....
# index error. That means that there is nothing in triangle? am I consuming tri? No, I only reference it, except for when I append at the very end. ok, well that assignment must be what is messing with it. so next row, does it have stuff in it? Well, yeah, it has 1 thing in it after the first trip. append only gets called once. Ok that is it. How does create an index error? next time through, when you slice where you slice, you see a problem. The next row needs to be bigger than the previous ....



