"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.



Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:

Input: head = [2,1], x = 2
Output: [1,2]


Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        current = head
        prev = dummy

        while current is not None and current.val < x:
            current = current.next
            prev = prev.next

        left_larger = current
        left_larger_prev = prev

        while current is not None:
            if current.val < x:
                tmp = current
                current = current.next
                # handle left handside
                left_larger_prev.next = tmp
                left_larger_prev.next.next = left_larger
                left_larger_prev = left_larger_prev.next
                # handle current
                prev.next = current
            else:
                current = current.next
                prev = prev.next

        return dummy.next
