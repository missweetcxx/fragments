#!/usr/bin/env python
# -*- coding: utf-8 -*-
from segments.linked_list.node import Node


class LinkedList(object):
    # set head node None
    def __init__(self):
        self.next = None

    # insert new node at start
    def insert_before(self, data):
        new_node = Node(data)
        new_node.set_next(self.next)
        self.next = new_node

    # insert new node at the end
    def insert_after(self, data):
        checking = self.next
        while checking is not None:
            if checking.get_next() is None:
                checking.set_next(Node(data))
                return
            checking = checking.get_next()
        else:
            self.next = Node(data)

    # search linked_list for data
    def search(self, data):
        checking = self.next  # from start point
        while checking is not None:
            if checking.get_data() == data:
                return True
            checking = checking.get_next()  # search the next node
        return False

    # delete node from linked_list
    def remove(self, data):
        checking = self.next  # search from start
        previous = None

        while checking is not None:
            if checking.get_data() == data:
                break
            previous = checking
            checking = checking.get_next()

        if previous is None:
            self.next = checking.get_next()
        else:
            previous.set_next(checking.get_next())

    def remove_all(self, data):
        checking = self.next
        previous = None

        while checking is not None:
            if checking.get_data() == data:
                if previous is None:
                    self.next = checking.get_next()
                else:
                    previous.set_next(checking.get_next())
            previous = checking
            checking = checking.get_next()

    def is_empty(self):
        return self.next is None

    # the size of linked_list
    def size(self):
        count = 0
        current = self.next
        while current is not None:
            count += 1
            current = current.get_next()
        return count
