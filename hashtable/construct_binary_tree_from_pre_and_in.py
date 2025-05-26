# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/?envType=problem-list-v2&envId=hash-table

# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        def helpe(preorder, inorder):
            if len(preorder) != len(inorder):
                raise ValueError("invalid tree encoding")
            if not preorder:
                return
            root_value = preorder[0]
            root = TreeNode(root_value)
            root_index_inorder = inorder.index(root_value)

            leftin = inorder[0:root_index_inorder]
            rightin = inorder[root_index_inorder + 1 :]
            leftpre = preorder[1 : root_index_inorder + 1]
            rightpre = preorder[root_index_inorder + 1 :]

            root.left = helpe(leftpre, leftin)
            root.right = helpe(rightpre, rightin)
            return root

        return helpe(preorder, inorder)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

tree = Solution().buildTree(preorder=preorder, inorder=inorder)

tosee = [tree]
while tosee:
    cur: TreeNode = tosee.pop(0)
    if not cur:
        print(" None ", end="")
        continue
    print(cur.val, end=" ")

    tosee.append(cur.left)
    tosee.append(cur.right)

print()
