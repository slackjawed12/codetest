# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        elem = []
        def search(root):
            if not root:
                return
            search(root.left)
            elem.append(root.val)
            search(root.right)

        search(root)
        result = TreeNode(elem[0], None, None)
        cur = result
        for e in elem[1:]:
            n = TreeNode(e, None, None)
            cur.right = n
            cur = n
        
        return result
            
            
            
                
        