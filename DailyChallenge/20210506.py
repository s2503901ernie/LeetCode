# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        array = []
        while head is not None:
            array.append(head.val)
            head = head.next
        
        return self.construct_tree(array)
        
    def construct_tree(self, array):
        if not array:
            return
        mid = math.floor((len(array) / 2))
        return TreeNode(
            val=array[mid], 
            left=self.construct_tree(array[0:mid]),
            right=self.construct_tree(array[mid+1:len(array)])
        )
    
