#
# Create on 4/18/2018
#
# Author: Sylvia
#

"""
101. Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.is_mirror(root.left, root.right)

    def is_mirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val == right.val:
            out_pair = self.is_mirror(left.left, right.right)
            in_piar = self.is_mirror(left.right, right.left)
            return out_pair and in_piar
        else:
            return False

    def isSymmetric2(self, root):
        if root is None:
            return True

        stack = [[root.left, root.right]]

        while len(stack) > 0:
            pair = stack.pop(0)
            left = pair[0]
            right = pair[1]

            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.insert(0, [left.left, right.right])

                stack.insert(0, [left.right, right.left])
            else:
                return False
        return True


from segments.binary_tree.binary_tree import BinaryTree


class Test:
    def test_true(self):
        s = BinaryTree()
        s.gen_tree([1, 2, 2, 3, 4, 4, 3, 1, 2, 3, 4, 4, 3, 2, 1])

        res = Solution()
        assert res.isSymmetric2(s.root) is True

    def test_false(self):
        s = BinaryTree()
        s.gen_tree([1, 2, 2, None, 3, None, 3])

        res = Solution()
        assert res.isSymmetric(s.root) is False
