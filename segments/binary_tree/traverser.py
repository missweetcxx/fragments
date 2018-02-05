#!/usr/bin/env python
# -*- coding: utf-8 -*-
from binary_tree import BinaryTree


class Traverser(BinaryTree):
    # Breadth-first Traverse (father node -> left child node -> right child node)
    def breadthFirst(self):
        nodeStack = [self.root, ]

        while len(nodeStack) > 0:
            my_node = nodeStack.pop()
            print(my_node.val)

            if my_node.left is not None:
                nodeStack.insert(0, my_node.left)

            if my_node.right is not None:
                nodeStack.insert(0, my_node.right)

    # Preorder Traverse (father node -> left child node -> right child node)
    def preorder(self, start_node):

        if start_node is None:
            return

        print(start_node.val)
        self.preorder(start_node.left)
        self.preorder(start_node.right)

    # Inorder Traverse(left child node -> father node -> right child node)
    def inorder(self, start_node):
        if start_node is None:
            return

        self.inorder(start_node.left)
        print(start_node.val)
        self.inorder(start_node.right)

    # Outorder Traverse(left child node -> right child node -> father node)
    def outorder(self, start_node):
        if start_node is None:
            return
        self.outorder(start_node.left)
        self.outorder(start_node.right)
        print(start_node.val)


def main():
    bt = Traverser()
    for i in range(10):
        bt.addNode(i)

    print("Breadth-first Traverse-->")
    bt.breadthFirst()

    print("Preorder Traverse-->")
    bt.preorder(bt.root)

    print("Inorder Traverse-->")
    bt.inorder(bt.root)

    print("Outorder Traverse-->")
    bt.outorder(bt.root)


if __name__ == '__main__':
    main()
