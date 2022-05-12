# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def swapPairs(self, head):
#         if not head or not head.next:
#             return head
#         temp = ListNode(0)
#         temp.next = head
#         curr = temp

#         while curr.next and curr.next.next:
#             fast = curr.next
#             slow = curr.next.next
#             fast.next = slow.next
#             curr.next = slow
#             curr.next.next = fast
#             curr = curr.next.next
#         return temp.next

from random import random, randrange


print([randrange(1,10) for i in range(3)])
