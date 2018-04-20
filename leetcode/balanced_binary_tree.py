#
# Create on 4/19/2018
#
# Author: Sylvia
#

"""
110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def check(root):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return 1
            elif root.left.val is None and root.right.val is None:
                return 1
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1


import pytest

from segments.binary_tree.binary_tree import BinaryTree


class Test:
    @pytest.mark.parametrize('nums, expect', [([3, 9, 20, None, None, 15, 7], True),
                                              ([1, 2, 2, None, None, 3, 3, None, None, None, None, 4], False),
                                              ([1, 2, 2, 3, 3, None, None, 4, 4], False)])
    def test(self, nums, expect):
        s = BinaryTree()
        s.gen_tree(nums)
        res = Solution()
        assert res.isBalanced(s.root) is expect
