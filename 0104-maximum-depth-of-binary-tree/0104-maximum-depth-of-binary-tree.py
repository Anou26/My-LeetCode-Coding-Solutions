# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Base case: if the node is None, the depth is 0
        if not root:
            return 0
        
        # Recursively find the depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # The depth of the tree rooted at this node is the greater of the
        # depths of the left and right subtrees plus one (for the current node)
        return max(left_depth, right_depth) + 1

# Example usage:
# Helper function to create a binary tree from a list
def create_binary_tree(lst, index=0):
    if index < len(lst):
        value = lst[index]
        if value is None:
            return None
        node = TreeNode(value)
        node.left = create_binary_tree(lst, 2 * index + 1)
        node.right = create_binary_tree(lst, 2 * index + 2)
        return node
    return None

# Create the binary tree from the example
tree = create_binary_tree([3, 9, 20, None, None, 15, 7])
solution = Solution()
print(solution.maxDepth(tree))  # Output: 3

# Another example
tree = create_binary_tree([1, None, 2])
print(solution.maxDepth(tree))  # Output: 2
