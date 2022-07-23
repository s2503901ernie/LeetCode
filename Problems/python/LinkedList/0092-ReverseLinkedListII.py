"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]


Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        current = head
        n = 1
        while n < left:
            current = current.next
            start = start.next
            n += 1
        prev = None
        while n <= right:
            tmp = current
            current = current.next
            tmp.next = prev
            prev = tmp
            n += 1
        start.next = prev
        tail = current
        current = prev
        while current:
            if current.next is None:
                current.next = tail
                break
            current = current.next

        return dummy.next


class Solution2:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l = []
        n = 1
        node = head
        last = None
        while node:
            if left <= n <= right:
                l.append(node)
            if n == right + 1:
                last = node
            node = node.next
            n += 1
        dummy = ListNode(0)
        dummy.next = head
        node = head
        pre = dummy
        n = 1
        while node:
            if n < left:
                node = node.next
                pre = pre.next
                n += 1
            elif n == left:
                for i in l[::-1]:
                    pre.next = i
                    pre = pre.next
                break
        pre.next = last
        return dummy.next
