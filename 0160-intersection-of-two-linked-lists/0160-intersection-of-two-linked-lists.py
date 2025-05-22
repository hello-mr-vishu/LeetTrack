# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # print(headA)
        # print(headB)
        if not headA or not headB:
            return None

        ptrA = headA
        ptrB = headB

        while ptrA != ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA

        return ptrA
        
        # def get_len(ptr):
        #     cnt = 0
        #     while ptr:
        #         cnt +=1
        #         ptr = ptr.next
        #     return cnt 

        # lenA = get_len(headA)
        # lenB = get_len(headB)
        # print(lenA)
        # print(lenB)

        # ptrA = headA
        # ptrB = headB

        # if lenA>lenB:
        #     for _ in range(lenA-lenB):
        #         ptrA = ptrA.next
        # else:
        #     for _ in range(lenB-lenA):
        #         ptrB = ptrB.next
        # while ptrA and ptrB:
        #     if ptrA == ptrB:
        #         return ptrA
        #     ptrA = ptrA.next
        #     ptrB = ptrB.next

        # return None













        # hs = set()
        # ptrA = headA
        # ptrB = headB
        # while ptrA:
        #     # cntA+=1
        #     print(hs)
        #     hs.add(ptrA)
        #     ptrA = ptrA.next
        # # while headB:
        # #     cntB+=1
        # #     ptrB = ptrB.next
        # print(hs)
        # while ptrB:
        #     if ptrB in hs:
        #         return ptrB
        #     ptrB = ptrB.next
        # return None





        # left = headA
        # right = headB
        # while left and right:
        #     # print(left.next)
        #     if left in hs:
        #         ret = left.next
        #         return ret
        #     if right in hs:
        #         ret = right.next
        #         return ret
        #     hs.add(left) 
        #     hs.add(right)
        #     # print(hs)
        #     print(left)
        #     print(right)
        #     left = left.next
        #     right = right.next
        # return None
        
        
        
        
    

        
        # if not headA or not headB:
        #     return None


        # def get_length(head):
        #     length = 0
        #     while head:
        #         length += 1
        #         head = head.next
        #     return length
        
        # lenA = get_length(headA)
        # lenB = get_length(headB)

        # currA = headA
        # currB = headB

        # if lenA > lenB:
        #     for _ in range(lenA - lenB):
        #         currA = currA.next
        # else:
        #     for _ in range(lenB - lenA):
        #         currB = currB.next

        # while currA and currB:
        #     if currA == currB:  
        #         return currA
        #     currA = currA.next
        #     currB = currB.next

        # return None 
