# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.prev = None
        self.min_diff = float('inf')
        self.inorder_traversal(root)
        return self.min_diff
    
    def inorder_traversal(self, node):
        if not node:
            return
        # Traverse the left subtree
        self.inorder_traversal(node.left)
        
        # Process the current node
        if self.prev is not None:
            self.min_diff = min(self.min_diff, node.val - self.prev.val)
        self.prev = node
        
        # Traverse the right subtree
        self.inorder_traversal(node.right)
