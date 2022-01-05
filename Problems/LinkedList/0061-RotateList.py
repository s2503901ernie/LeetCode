"""
Given the head of a linked list, rotate the list to the right by k places.


Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]


Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 10^9
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        current = head
        length = 0
        while current:
            length += 1
            if current.next is None:
                current.next = head
                break
            current = current.next
        k = length - (k % length)
        previous = current
        current = head
        n = 0
        while n < k:
            current = current.next
            previous = previous.next
            n += 1
        previous.next = None

        return current
