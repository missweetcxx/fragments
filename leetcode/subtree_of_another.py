#
# Create on 4/12/2018
#
# Author: Sylvia
#

"""
572. Subtree of Another Tree
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a 
subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also
be considered as a subtree of itself.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if self.isMatch(s, t): return True
        if not s: return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isMatch(self, s, t):
        if not (s and t):
            return s is t
        return (s.val == t.val and
                self.isMatch(s.left, t.left) and
                self.isMatch(s.right, t.right))

    def isSubtree_2(self, s, t):
        from hashlib import sha256
        def hash_(x):
            S = sha256()
            S.update(x.encode())
            return S.hexdigest()

        def merkle(node):
            if not node:
                return '#'
            m_left = merkle(node.left)
            m_right = merkle(node.right)
            node.merkle = hash_(m_left + str(node.val) + m_right)
            return node.merkle

        merkle(s)
        merkle(t)

        def dfs(node):
            if not node:
                return False
            return (node.merkle == t.merkle or
                    dfs(node.left) or dfs(node.right))

        return dfs(s)


from segments.binary_tree.binary_tree import BinaryTree


class Test:
    def test_true(self):
        s = BinaryTree()
        for x in [1, 2, 3, 4, 5]:
            s.addNode(x)

        t = BinaryTree()
        for x in [2, 4, 5]:
            t.addNode(x)

        res = Solution()
        assert res.isSubtree_2(s.root, t.root) is True

    def test_false(self):
        s = BinaryTree()
        for x in [1, 2, 3, 4, 5]:
            s.addNode(x)
        t = BinaryTree()
        for x in [2, 5, 4]:
            t.addNode(x)

        res = Solution()
        assert res.isSubtree_2(s.root, t.root) is False
