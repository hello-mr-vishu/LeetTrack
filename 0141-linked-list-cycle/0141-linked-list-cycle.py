# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head.next == None:
            return False
        hashset = set()
        curr = head
        while curr:
            if curr.next in hashset:
                return True
            hashset.add(curr.next)
            curr = curr.next
        return False