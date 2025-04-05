# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        lst = []
        while temp:
            lst.append(temp.val)
            temp = temp.next
        lst.sort()
        temp = head
        i= 0
        while temp:
            temp.val = lst[i]
            i+=1
            temp = temp.next
        return head