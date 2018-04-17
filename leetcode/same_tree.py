#
# Create on 4/17/2018
#
# Author: Sylvia
#

"""
100. Same Tree
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not (p and q):
            return p is None and q is None
        return (p.val == q.val and
                self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left))

    def isSameTree2(self, p, q):
        from hashlib import sha1

        def hash_sha1(x):
            s = sha1()
            s.update(x.encode('utf-8'))
            return s.hexdigest().upper()

        def merkle(node):
            if not node:
                return '#'
            m_left = merkle(node.left)
            m_right = merkle(node.right)
            node.merkle = hash_sha1(m_left + str(node.val) + m_right)
            return node.merkle

        return merkle(p) == merkle(q)


from segments.binary_tree.binary_tree import BinaryTree


class Test:
    def test_true(self):
        s = BinaryTree()
        for x in [1, 2, 4, 1]:
            s.addNode(x)
        t = s
        res = Solution()
        assert res.isSameTree(s.root, t.root) is True

    def test_false(self):
        s = BinaryTree()
        for x in [1, 2, 3, 4, 5]:
            s.addNode(x)
        t = BinaryTree()
        for x in [1, 3, 2, 3]:
            t.addNode(x)
        res = Solution()
        assert res.isSameTree2(s.root, t.root) is False
