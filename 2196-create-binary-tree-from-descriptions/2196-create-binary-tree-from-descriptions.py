# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        store = {}
        root = None
        for p, c, left in descriptions:
            ct = TreeNode(c, None, None) if c not in store else store[c][0]
            pt = TreeNode(p, None, None) if p not in store else store[p][0]
            
            if left:
                pt.left = ct
            else:
                pt.right = ct
            
            store[c] = (ct, p)
            store[p] = (pt, None) if p not in store else (pt, store[p][1])

        for k, v in store.items():
            if not v[1]:
                root = v[0]
        
        return root