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
        def helpe(inorder, preorder):
            if not inorder or not preorder:
                return None

            root_val = preorder.pop(0)
            root = TreeNode(root_val)

            index = inorder.index(root_val)

            root.left = helpe(inorder[:index], preorder[:index])
            root.right = helpe(inorder[index + 1 :], preorder[index:])
            return root

        return helpe(inorder, preorder)


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
