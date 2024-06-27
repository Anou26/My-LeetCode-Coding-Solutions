# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to serve as the starting point of the merged list
        dummy = ListNode()
        current = dummy

        # Traverse both lists and compare each pair of nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # If any elements are left in either list, append them
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Return the merged list starting from the node after the dummy node
        return dummy.next

# Example usage:
# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)
print_linked_list(merged_list)  # Output: [1, 1, 2, 3, 4, 4]
