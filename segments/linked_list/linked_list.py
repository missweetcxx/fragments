#!/usr/bin/env python
# -*- coding: utf-8 -*-
from segments.linked_list.node import Node


class LinkedList(object):
    # set head node None
    def __init__(self):
        self.head = None

    # insert new node at start
    def add_head(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    # insert new node at the end
    def add_tail(self, data):
        checking = self.head
        while checking is not None:
            if checking.get_next() is None:
                checking.set_next(Node(data))
                return
            checking = checking.get_next()
        else:
            self.head = Node(data)

    # search linked_list for data
    def search(self, data):
        checking = self.head  # from start point
        while checking is not None:
            if checking.get_data() == data:
                return True
            checking = checking.get_next()  # search the next node
        return False

    # delete node from linked_list
    def remove(self, data):
        checking = self.head  # search from start
        previous = None

        while checking is not None:
            if checking.get_data() == data:
                break
            previous = checking
            checking = checking.get_next()

        if previous is None:
            self.head = checking.get_next()
        else:
            previous.set_next(checking.get_next())


def is_empty(self):
    return self.head is None


# the size of linked_list
def size(self):
    count = 0
    counting = self.head
    while counting is not None:
        count += 1
        counting = counting.get_next()
    return count


link = LinkedList()
link.add_head(1)
link.add_head(2)
link.add_head(3)
link.add_tail(4)
link.add_tail(5)
link.remove(2)

