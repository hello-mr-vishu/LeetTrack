class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases like removing the head
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Move fast n+1 steps ahead so the gap between slow and fast is n
        for _ in range(n + 1):
            fast = fast.next

        # Move both fast and slow one step at a time until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Now, slow is just before the node to delete
        slow.next = slow.next.next

        return dummy.next
