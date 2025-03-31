# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        temp = head
        count = 0
        while temp is not None:
            count +=1
            temp = temp.next
        temp = head
        mid = count//2 +1
        while temp is not None:
            mid = mid-1
            if mid == 0:
                break
            temp = temp.next
        return temp