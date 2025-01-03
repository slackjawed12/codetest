# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.helper(preorder, 0, len(preorder)-1)
    
    def helper(self, arr:List[int], left:int, right:int) -> Optional[TreeNode]:
        if left > right:
            return None
        
        root = TreeNode(arr[left], None, None)
        nr = right
        while arr[nr] > root.val:
            nr -= 1

        root.left = self.helper(arr, left+1, nr)
        root.right = self.helper(arr, nr+1, right)
        return root
    