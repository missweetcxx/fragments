#!/usr/bin/env python
# -*- coding: utf-8 -*-
from segments.linked_list.node import Node


class OrderedLinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, data):
        checking = self.head
        previous = None
        while checking is not None:
            if checking.get_data() > data:
                break
            previous = checking
            checking = checking.get_next()

        new_node = Node(data)
        if previous is None:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            previous.set_next(new_node)
            new_node.set_next(checking)


def search(self, data):
    checking = self.head
    while checking is not None:
        if checking.get_data() == data:
            return True
        elif checking.get_data() > data:
            return False
        checking = checking.get_next()
    return False


def remove(self, data):
    checking = self.head
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


def size(self):
    count = 0
    counting = self.head
    while counting is not None:
        count += 1
        counting = counting.get_next()
    return count
