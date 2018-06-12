#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .linked_list import LinkedList, Node


def reverse_linked_list_a(head):
    # 将链表放进数组，再构造新链表，空间损耗大
    if head is None or head.next is None:
        return head
    arr = []
    while head:
        arr.append(head.data)
        head = head.next
    new_head = LinkedList()
    tmp = new_head
    for item in arr[::-1]:
        tmp.next = Node(item)
        tmp = tmp.next
    return new_head.next


def reverse_linked_list_b(head):
    if not head or not head.next:
        return head
    pre = None
    while head:
        next = head.next  # 缓存当前节点的向后指针，下次迭代用
        head.next = pre  # 把当前节点的向前指针作为当前节点的向后指针
        pre = head  # 作为下次迭代(当前节点)的向前指针
        head = next  # 作为下次迭代的(当前)节点
    return pre


def reverse_linked_list_c(head):
    if head is None or head.next is None:
        return head
    p1 = head
    p2 = head.next
    while p2:
        tmp = p2.next
        p2.next = p1
        p1 = p2
        p2 = tmp
    head.next = None
    return p1


def reverse_linked_list_d(head):
    if head is None or head.next is None:
        return head
    else:
        new_head = reverse_linked_list_d(head.next)
        head.next.next = head
        head.next = None
    return new_head
