#
# Create on 6/12/2018
#
# Author: Sylvia
#

"""
404. Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root, is_left=False):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            if Solution.is_none(root) and is_left:
                return root.val
            return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right)
        return 0

    @staticmethod
    def is_none(node):
        if not node.left and not node.right:
            return True
        elif hasattr(node.left, 'val') and hasattr(node.right, 'val'):
            if not node.left.val and not node.right.val:
                return True


from segments.binary_tree.binary_tree import BinaryTree


class Test:
    def test(self):
        s = BinaryTree()
        s.gen_tree([3, 9, 20, None, None, 15, 7])

        res = Solution()
        assert res.sumOfLeftLeaves(root=s.root) is 24
