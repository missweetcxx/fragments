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
    def addNode(self, val):
        # create root node of binary tree
        nodeStack = [self.root, ]

        # if root node hasn't been created
        if self.root == None:
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
