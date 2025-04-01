# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next == None:
            return head
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        # print(stack)
        curr = head
        # print(head)
        while stack:
            curr.val = stack.pop()
            # print(stack)
            curr = curr.next

        print(curr)

            # temp = temp.next
        return head