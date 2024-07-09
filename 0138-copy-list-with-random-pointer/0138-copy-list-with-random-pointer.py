# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        # Step 1: Create new nodes and interweave them with original nodes
        current = head
        while current:
            new_node = Node(current.val, current.next)
            current.next = new_node
            current = new_node.next
        
        # Step 2: Assign random pointers for the new nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        # Step 3: Separate the new nodes to form the new linked list
        current = head
        new_head = head.next
        while current:
            new_node = current.next
            current.next = new_node.next
            if new_node.next:
                new_node.next = new_node.next.next
            current = current.next
        
        return new_head

# Example usage:
# Let's create a linked list and test the function
def print_list(head):
    nodes = []
    while head:
        random_index = None if not head.random else head.random.val
        nodes.append([head.val, random_index])
        head = head.next
    print(nodes)

# Create an example linked list: [[7,null],[13,0],[11,4],[10,2],[1,0]]
node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node2.random = node1
node3.random = node5
node4.random = node3
node5.random = node1

print_list(node1)
solution = Solution()
copied_head = solution.copyRandomList(node1)
print_list(copied_head)
