#
# Create on 4/16/2018
#
# Author: Sylvia
#

"""
234. Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import copy

from leetcode.reverse_linked_list import Solution as Reverse_Solution


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp = copy.deepcopy(head)
        res = Reverse_Solution()
        r_head = res.reverseList2(temp)
        while head and r_head:
            if r_head.data != head.data:
                return False
            r_head = r_head.next
            head = head.next
        return True

    def isPalindrome2(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node = None
        while slow:
            current = slow
            slow = slow.next
            current.next = node
            node = current
        while node:
            if node.data != head.data:
                return False
            node = node.next
            head = head.next
        return True


from segments.linked_list.linked_list import LinkedList


def test_true():
    head = LinkedList()
    input_list = [1, 2, 3, 2, 1]
    for item in input_list:
        head.insert_after(item)
    res = Solution()
    assert res.isPalindrome2(head.next) is True


def test_false():
    head = LinkedList()
    input_list = [1, 2, 3]
    for item in input_list:
        head.insert_after(item)
    res = Solution()
    assert res.isPalindrome2(head.next) is False
