# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Function to reverse a linked list between head and tail
        def reverse(head, tail):
            prev = None
            curr = head
            while curr != tail:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        # Function to get the k-th node from the current node
        def getKthNode(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr
        
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            kth = getKthNode(group_prev, k)
            if not kth:
                break
            group_next = kth.next
            # Reverse the group
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
        
        return dummy.next
