class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

headA = ListNode([4,1,8,4,5])
headB = ListNode([5,6,1,8,4,5])

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        seen = {}
        dummy1 = headB
        while dummy1:
            seen[dummy1] = dummy1
            dummy1 = dummy1.next
        dummy2 = headA
        while dummy2:
            if dummy2 in seen:
                return dummy2
            dummy2 = dummy2.next
        return None

obj = Solution()
print(obj.getIntersectionNode(headA, headB))