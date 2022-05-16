"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.


Follow up: Could you solve it without reversing the input lists?
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        length1 = 0
        length2 = 0
        cur1 = l1
        cur2 = l2
        while cur1:
            length1 += 1
            cur1 = cur1.next
        while cur2:
            length2 += 1
            cur2 = cur2.next
        cur1 = l1
        cur2 = l2
        if length1 >= length2:
            startfroml1 = True
        else:
            startfroml1 = False
        if startfroml1 is True:
            while length1 > length2:
                cur1 = cur1.next
                length1 -= 1
        else:
            while length2 > length1:
                cur2 = cur2.next
                length2 -= 1
        while cur1 and cur2:
            cur1.val = cur1.val + cur2.val
            cur2.val = cur1.val
            cur1 = cur1.next
            cur2 = cur2.next
        dummy = ListNode(0)
        prev = dummy
        if startfroml1 is True:
            dummy.next = l1
            cur = l1
        else:
            dummy.next = l2
            cur = l2
        cycle = True
        while cycle is True:
            cycle = False
            while cur:
                if cur.val >= 10:
                    prev.val += 1
                    cur.val -= 10
                if prev.val >= 10:
                    cycle = True
                cur = cur.next
                prev = prev.next
            prev = dummy
            if startfroml1 is True:
                cur = l1
            else:
                cur = l2

        if dummy.val > 0:
            return dummy
        else:
            return dummy.next


class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        cur = l1
        while cur:
            stack1.append(cur.val)
            cur = cur.next
        cur = l2
        while cur:
            stack2.append(cur.val)
            cur = cur.next
        carry = 0
        cur = None
        while stack1 or stack2 or carry != 0:
            total = 0
            if stack1:
                total += stack1.pop()
            if stack2:
                total += stack2.pop()
            total += carry
            carry, added = divmod(total, 10)
            new = ListNode(added)
            new.next = cur
            cur = new

        return cur
