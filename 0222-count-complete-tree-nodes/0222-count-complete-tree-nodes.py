# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)
    
    def helper(self, root: Optional[TreeNode], result: int) -> int:
        if root is None:
            return result
        
        result += 1
        result = self.helper(root.left, result)
        result = self.helper(root.right, result)
        return result
        
        
    
        