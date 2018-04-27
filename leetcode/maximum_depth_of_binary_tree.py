#
# Create on 4/19/2018
#
# Author: Sylvia
#

"""
104. Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)


import pytest

from segments.binary_tree.binary_tree import BinaryTree


class Test:
    @pytest.mark.parametrize('nums, expect', [([3, 9, 20, None, None, 15, 7], 3),
                                              ([1, 2, None, 3, None, 4, None, 5], 4),
                                              ([], 0),
                                              ([5, 4, 7, 3, None, 2, None, -1, None, 9], 4)])
    def test(self, nums, expect):
        s = BinaryTree()
        s.gen_tree(nums)
        res = Solution()
        assert res.maxDepth(s.root) is expect
