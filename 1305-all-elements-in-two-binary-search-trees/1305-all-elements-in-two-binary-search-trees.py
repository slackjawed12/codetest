# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        result = []
        def traverse(root):
            if not root:
                return

            traverse(root.left)
            result.append(root.val)
            traverse(root.right)
        
        traverse(root1)
        traverse(root2)
        result.sort()
        return result