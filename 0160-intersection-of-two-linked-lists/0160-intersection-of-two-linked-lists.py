# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None


        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        lenA = get_length(headA)
        lenB = get_length(headB)

        currA = headA
        currB = headB

        if lenA > lenB:
            for _ in range(lenA - lenB):
                currA = currA.next
        else:
            for _ in range(lenB - lenA):
                currB = currB.next

        while currA and currB:
            if currA == currB:  
                return currA
            currA = currA.next
            currB = currB.next

        return None 
