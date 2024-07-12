# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            # If the list is empty or has only one node, return None
            return None
        
        # Initialize slow and fast pointers
        slow, fast = head, head
        prev = None
        
        # Move fast pointer twice as fast as slow pointer
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Delete the middle node
        if prev:
            prev.next = slow.next
        
        return head

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list to a list of values
def linked_list_to_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

# Example usage:
sol = Solution()

# Test case 1
head = create_linked_list([1, 3, 4, 7, 1, 2, 6])
result_head = sol.deleteMiddle(head)
print(linked_list_to_list(result_head))  # Output: [1, 3, 4, 1, 2, 6]

# Test case 2
head = create_linked_list([1, 2, 3, 4])
result_head = sol.deleteMiddle(head)
print(linked_list_to_list(result_head))  # Output: [1, 2, 4]

# Test case 3
head = create_linked_list([2, 1])
result_head = sol.deleteMiddle(head)
print(linked_list_to_list(result_head))  # Output: [2]
