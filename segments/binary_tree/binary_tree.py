#!/usr/bin/env python
# -*- coding: utf-8 -*-

from segments.binary_tree.node import Node


class BinaryTree(object):
    """
    generate binary tree
    """

    def __init__(self):
        self.root = None
        pass

    # create a binary tree with nodes
    def _add_node(self, val):
        # create root node of binary tree
        nodeStack = [self.root, ]

        # if root node hasn't been created
        if self.root is None:
            self.root = Node(val)
            print("Successfully add root node as {0}!".format(self.root.val))
            return

        while len(nodeStack) > 0:
            # pop node stack
            p_node = nodeStack.pop()

            # if left child node not exist
            if p_node.left is None:
                p_node.left = Node(val)
                print("Add left node as {0} ".format(p_node.left.val))
                return

            # if right child node not exist
            if p_node.right is None:
                p_node.right = Node(val)
                print("Add right node as {0} ".format(p_node.right.val))
                return

            nodeStack.insert(0, p_node.left)
            nodeStack.insert(0, p_node.right)

    def gen_tree(self, nums):
        for x in nums:
            self._add_node(x)

            # def __init__(self):
            #     self.root = Node(None)
            #     self.myQueue = []
            #
            # def add_node(self, elem):
            #     node = Node(elem)
            #     if self.root.val is None:
            #         self.root = node
            #         self.myQueue.append(self.root)
            #     else:
            #         tree_node = self.myQueue[0]
            #         if tree_node.left is None:
            #             tree_node.left = node
            #             self.myQueue.append(tree_node.left)
            #         else:
            #             tree_node.right = node
            #             self.myQueue.append(tree_node.right)
            #             self.myQueue.pop(0)
