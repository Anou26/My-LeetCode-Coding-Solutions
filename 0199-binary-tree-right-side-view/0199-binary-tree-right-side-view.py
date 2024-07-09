# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        from collections import deque

        queue = deque([root])
        right_view = []

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                # If this is the last node in the current level, add it to the right view
                if i == level_length - 1:
                    right_view.append(node.val)
                # Add left and right children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return right_view

# Example usage:
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.right = TreeNode(5)
# root.right.right = TreeNode(4)

# solution = Solution()
# print(solution.rightSideView(root))  # Output: [1, 3, 4]
