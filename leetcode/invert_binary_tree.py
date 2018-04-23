#
# Create on 4/23/2018
#
# Author: Sylvia
#

"""
226. Invert Binary Tree
Invert a binary tree.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.invert(root)
        return root

    def invert(self, root):
        if root is None:
            return

        right_node = root.right
        left_node = root.left

        root.right = left_node
        root.left = right_node

        self.invert(root.left)
        self.invert(root.right)


import pytest

from segments.binary_tree.binary_tree import BinaryTree


class Test:
    @pytest.mark.parametrize('nums, expect', [([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
                                              ([3, 2, None], [3, None, 2])])
    def test_is_same(self, nums, expect):
        s = BinaryTree()
        s.gen_tree(nums)

        e_s = BinaryTree()
        e_s.gen_tree(expect)

        res = Solution()
        new_node = res.invertTree(s.root)
        assert self.is_same(new_node, e_s.root)

    def is_same(self, p, q):
        if not (p and q):
            return p is None and q is None
        return p.val == q.val and self.is_same(p.right, q.right) and self.is_same(p.left, q.left)
