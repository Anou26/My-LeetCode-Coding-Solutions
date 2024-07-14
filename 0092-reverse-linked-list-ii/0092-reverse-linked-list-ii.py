# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head or left == right:
            return head
        
        # Create a dummy node to handle edge cases easily
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move prev to the node just before the left position
        for _ in range(left - 1):
            prev = prev.next
        
        # Start reversing the sublist
        reverse_start = prev.next
        current = reverse_start.next
        
        # Reverse the nodes from left to right
        for _ in range(right - left):
            reverse_start.next = current.next
            current.next = prev.next
            prev.next = current
            current = reverse_start.next
        
        return dummy.next
