# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        
        # The last element in postorder list is the root
        root_val = postorder.pop()
        root = TreeNode(root_val)
        
        # Find the index of the root in inorder list
        inorder_index = inorder.index(root_val)
        
        # Recursively build the right subtree and left subtree
        # Note: it's important to build the right subtree first because we are reducing postorder from the end
        root.right = self.buildTree(inorder[inorder_index+1:], postorder)
        root.left = self.buildTree(inorder[:inorder_index], postorder)
        
        return root
