# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        stack = []
        while temp:
            stack.append(temp.val)
            temp = temp.next
        temp = head
        while temp:
            if temp.val != stack.pop():
                return False
            temp = temp.next
        return True