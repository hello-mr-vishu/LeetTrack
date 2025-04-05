# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 0
        curr = head
        while curr:
            cnt +=1
            curr = curr.next
        
        if n == cnt :
            return head.next
        cnt1 = cnt-n
        # print(cnt,cnt1)
        curr = head
        # print(type(curr))
        for _ in range(cnt - n - 1):
            curr = curr.next
        if curr.next:    
            curr.next = curr.next.next
        # curr.next.next = None
        return head
