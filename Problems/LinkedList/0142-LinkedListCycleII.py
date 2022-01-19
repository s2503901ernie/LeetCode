"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.



Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


Constraints:

The number of the nodes in the list is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    """
    O(n) time
    O(n) space

    n is the length of the linked list.
    """
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        board = set()
        cur = head
        while cur is not None:
            if cur not in board:
                board.add(cur)
            else:
                return cur
            cur = cur.next

        return None


class Solution2:
    """
    O(n) time
    O(1) space

    n is the length of the linked list.
    """
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return None
        first = head.next
        second = head.next.next
        while first and second and second.next and first != second:
            first = first.next
            second = second.next

        if not first or not second or not second.next:
            return None

        first = head
        while first and second and first != second:
            first = first.next
            second = second.next

        return first
