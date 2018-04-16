#
# Create on 4/16/2018
#
# Author: Sylvia
#

"""
205. Reverse Linked List
Reverse a singly linked list.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous = None
        while head:
            temp = head
            temp.next = previous
            previous = temp
            head = head.next
        return previous

    def reverseList2(self, head):
        return self._reverse(head)

    def _reverse(self, node, previous=None):
        if not node:
            return previous
        follow = node.next
        node.next = previous
        return self._reverse(follow, node)


from segments.linked_list.linked_list import LinkedList


class Test:
    def test_normal(self):
        head = LinkedList()
        input_list = [1, 2, 3, 4, 5]
        point = len(input_list) - 1
        for x in input_list:
            head.insert_after(x)
        res = Solution()
        output = res.reverseList(head.next)
        while output.next is not None:
            assert output.data is input_list[point]
            output = output.next
            point -= 1

    def test_empty(self):
        head = LinkedList()
        res = Solution()
        output = res.reverseList(head.next)
        assert output is None
