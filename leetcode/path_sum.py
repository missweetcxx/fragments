#
# Create on 4/23/2018
#
# Author: Sylvia
#

"""
112. Path Sum
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along
the path equals the given sum.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


from segments.binary_tree.binary_tree import BinaryTree


class Test:
    def test_true(self):
        s = BinaryTree()
        s.gen_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1])
        res = Solution()
        assert res.hasPathSum(s.root, 22) is True

    def test_false(self):
        s = BinaryTree()
        s.gen_tree([3, 4, 2, 7, 3, 1, 8])
        res = Solution()
        assert res.hasPathSum(s.root, 99) is False
