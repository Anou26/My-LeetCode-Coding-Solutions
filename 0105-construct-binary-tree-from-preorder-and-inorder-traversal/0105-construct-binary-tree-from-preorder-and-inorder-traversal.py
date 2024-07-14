# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        
        # Create a map to store the index of each value in the inorder list
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(preorder_start, preorder_end, inorder_start, inorder_end):
            if preorder_start > preorder_end or inorder_start > inorder_end:
                return None
            
            # The first element in preorder list is the root node
            root_val = preorder[preorder_start]
            root = TreeNode(root_val)
            
            # Find the index of the root in the inorder list
            inorder_root_index = inorder_index_map[root_val]
            
            # Calculate the number of nodes in the left subtree
            left_subtree_size = inorder_root_index - inorder_start
            
            # Recursively build the left subtree
            root.left = build(preorder_start + 1, preorder_start + left_subtree_size, inorder_start, inorder_root_index - 1)
            
            # Recursively build the right subtree
            root.right = build(preorder_start + left_subtree_size + 1, preorder_end, inorder_root_index + 1, inorder_end)
            
            return root
        
        # Initialize the recursive function
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
