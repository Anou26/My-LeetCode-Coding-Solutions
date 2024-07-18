# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = float('-inf')  # Initialize to the smallest possible value
        
        def max_gain(node):
            if not node:
                return 0
            
            # Recursively get the maximum sum of the left and right subtrees
            # If the computed gain is negative, discard it by taking max with 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # Current path sum including the node and both subtrees
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum path sum
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the maximum gain that can be obtained by including the current node
            return node.val + max(left_gain, right_gain)
        
        # Start the recursion from the root
        max_gain(root)
        
        return self.max_sum
