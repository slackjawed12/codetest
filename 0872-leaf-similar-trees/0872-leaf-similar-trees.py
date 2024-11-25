# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(root, result):
            if not root:
                return
            
            if not root.left and not root.right:
                result.append(root.val)
            
            leaves(root.left, result)
            leaves(root.right, result)
        
        leaves1, leaves2 = [], []
        leaves(root1, leaves1)
        leaves(root2, leaves2)
        if len(leaves1) != len(leaves2):
            return False
        
        for i in range(len(leaves1)):
            if leaves1[i] != leaves2[i]:
                return False

        return True