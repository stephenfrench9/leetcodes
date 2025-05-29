# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/?envType=problem-list-v2&envId=hash-table

# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution0:
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


class Solution:
    """
    This solution is the same strategy as the above, where the pre and in lists are passed to each function call explicitly, except it is indices only that are passed, to save memory and in the end the time it takes to make a ton of lists.

    There is yet another solution possible, where you pass only the inorder list indices, and consume from the global preorder list. The end result is that each function in the call stack is lighter. This is conceptually more tricky to understand - you must convince your self that the preorder lists will be managed correctly because you are building the tree with a preorder traversal. The effect is that each call has a value from the preorder list that is the root of the subtree represented by the inorder list handed to it as an argument. Said another way, the way you build the callstack is in an inorder way - first the root, then then root of the leftsubtree, then the left of the right subtree, then the root of the left subtree of the left subtree, and the root of the right  .... and this is the same order of the roots that come out of the preorder list.
    """

    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        inoindex = {value: index for index, value in enumerate(inorder)}

        def supa(preo, ino):

            if preo[1] - preo[0] != ino[1] - ino[0]:
                raise ValueError("invalid tree encoding")
            if preo[1] == preo[0]:
                return

            root_value = preorder[preo[0]]
            root = TreeNode(root_value)
            root_index_ino = inoindex[root_value]

            ino_left = (ino[0], root_index_ino)
            num_nodes_left = ino_left[1] - ino_left[0]
            ino_right = (root_index_ino + 1, ino[1])
            num_nodes_right = ino_right[1] - ino_right[0]

            pre_left = (preo[0] + 1, preo[0] + 1 + num_nodes_left)
            pre_right = (preo[0] + 1 + num_nodes_left, preo[1])

            root.left = supa(pre_left, ino_left)
            root.right = supa(pre_right, ino_right)
            return root

        return supa((0, len(preorder)), (0, len(inorder)))


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
