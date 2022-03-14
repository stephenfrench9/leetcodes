# www.leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        explore = [root]

        total = 0
        while explore:
            step = explore.pop()
            if low <= step.val and step.val <= high:
                total += step.val

            if step.left and low < step.val:
                explore.append(step.left)

            if step.right and step.val < high:
                explore.append(step.right)

        return total