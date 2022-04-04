"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]


Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 10^5
0 <= Node.val <= 100
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Calculate length and back_k
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        back_k = length - k + 1
        # get swap1 and swap2
        dummy = ListNode
        prev = dummy
        prev.next = head
        cur = head
        position = 0
        while cur:
            position += 1
            if position == k:
                swap1 = cur
                prev1 = prev
            if position == back_k:
                swap2 = cur
                prev2 = prev
            cur = cur.next
            prev = prev.next
        # swap nodes
        prev1.next = swap2
        prev2.next = swap1
        swap1.next, swap2.next = swap2.next, swap1.next

        return dummy.next


class Solution2:
    """
    Use value exchange
    """
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        right = head
        checker = head
        for i in range(k-1):
            checker = checker.next
        left = checker
        while checker.next:
            checker = checker.next
            right = right.next
        left.val, right.val = right.val, left.val

        return head


class Solution3:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode
        dummy.next = head
        prev_left = dummy
        prev_right = dummy
        right = head
        checker = head
        for i in range(k-1):
            checker = checker.next
            prev_left = prev_left.next
        left = checker
        while checker.next:
            checker = checker.next
            right = right.next
            prev_right = prev_right.next
        prev_left.next, prev_right.next = right, left
        left.next, right.next = right.next, left.next

        return dummy.next
