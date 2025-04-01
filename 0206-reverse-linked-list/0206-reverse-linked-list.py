# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # temp = ListNode(0)
        prev = None
        curr = head
        # print(type(prev))
        # print(curr)
        # print(temp)
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev