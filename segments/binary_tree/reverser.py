#!/usr/bin/env python
# -*- coding: utf-8 -*-
from segments.binary_tree.traverser import Traverser


class Reverse(Traverser):
    def reverse_tree(self, root):
        if not root:
            return
        # get left and right node
        tmp_left_node = root.left
        tmp_right_node = root.right

        # reverse
        root.left = tmp_right_node
        root.right = tmp_left_node

        # recurse
        self.reverse_tree(root.left)
        self.reverse_tree(root.right)


def main():
    node = Reverse()
    for i in range(1, 8):
        node.addNode(i)

    node.breadthFirst()

    node.reverse_tree(node.root)

    print("Result : ")
    node.breadthFirst()


if __name__ == '__main__':
    main()
