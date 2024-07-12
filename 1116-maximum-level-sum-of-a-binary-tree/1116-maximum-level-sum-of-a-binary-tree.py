from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        # Initialize queue for BFS
        queue = deque([(root, 1)])  # (node, level)
        level_sums = {}
        
        while queue:
            node, level = queue.popleft()
            
            if level in level_sums:
                level_sums[level] += node.val
            else:
                level_sums[level] = node.val
            
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        # Find the level with the maximum sum
        max_level = max(level_sums, key=lambda x: (level_sums[x], -x))
        
        return max_level

# Helper function to create a binary tree from a list of values (for testing)
def create_binary_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

# Example usage:
# Example 1
root = create_binary_tree([1,7,0,7,-8,None,None])
sol = Solution()
print(sol.maxLevelSum(root))  # Output: 2

# Example 2
root = create_binary_tree([989,None,10250,98693,-89388,None,None,None,-32127])
sol = Solution()
print(sol.maxLevelSum(root))  # Output: 2
