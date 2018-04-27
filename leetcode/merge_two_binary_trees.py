#
# Create on 4/23/2018
#
# Author: Sylvia
#

"""
617. Merge Two Binary Trees
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are
overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as
the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
"""

from segments.binary_tree.binary_tree import BinaryTree
from segments.binary_tree.node import Node


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        t1_val, t2_val = 0, 0
        if t1: t1_val = t1.val if t1.val is not None else 0
        if t2: t2_val = t2.val if t2.val is not None else 0
        if t1_val == 0 and t2_val == 0:
            ans = Node(None)
        else:
            ans = Node(t1_val + t2_val)
        ans.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        ans.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
        return ans


import pytest


class Test:
    @pytest.mark.parametrize('t1, t2, expect', [([1, 3, 2, 5], [2, 1, 3, None, 4, None, 7], [3, 4, 5, 5, 4, None, 7])])
    def test_equal(self, t1, t2, expect):
        t1_tree = BinaryTree()
        t1_tree.gen_tree(t1)

        t2_tree = BinaryTree()
        t2_tree.gen_tree(t2)

        ex_tree = BinaryTree()
        ex_tree.gen_tree(expect)

        res = Solution()
        actual = res.mergeTrees(t1_tree.root, t2_tree.root)
        assert self.is_same(actual, ex_tree.root)

    def is_same(self, p, q):
        if not (p and q):
            return p is None and q is None
        return p.val == q.val and self.is_same(p.right, q.right) and self.is_same(p.left, q.left)
