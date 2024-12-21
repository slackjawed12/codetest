# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(r1, r2, level):
            if not r1 or not r2:
                return

            if level % 2 == 0:
                r2.val, r1.val = r1.val, r2.val
            
            invert(r1.left, r2.right, level + 1)
            invert(r2.left, r1.right, level + 1)
        
        invert(root.left, root.right, 0)
        
        return root