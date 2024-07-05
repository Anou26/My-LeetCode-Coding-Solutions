# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Initialize the dummy head of the resulting linked list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Traverse both linked lists
        while l1 is not None or l2 is not None:
            # Get the values from the current nodes, if present
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # Calculate the sum of the values and the carry
            total = val1 + val2 + carry
            carry = total // 10  # Update the carry for the next iteration
            total = total % 10  # Get the last digit of the sum
            
            # Create a new node with the sum and add it to the result list
            current.next = ListNode(total)
            current = current.next
            
            # Move to the next nodes in the input lists
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        # If there's a carry left after the final addition, add a new node
        if carry > 0:
            current.next = ListNode(carry)
        
        # Return the resulting linked list, starting from the next node of dummy head
        return dummy_head.next
