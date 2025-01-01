# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []
        def search(root: Optional[TreeNode]):
            if root is not None:
                search(root.left)
                nodes.append(root.val)
                search(root.right)

        search(root)
        return self.helper(nodes, 0, len(nodes)-1)

    def helper(self, nodes: List[int], left:int, right:int) -> Optional[TreeNode]:
        if left > right:
            return None
        
        mid = (left+right) // 2
        val = nodes[mid]
        node = TreeNode(val, None,None)
        node.left = self.helper(nodes, left, mid-1)
        node.right = self.helper(nodes, mid+1, right)
        return node
                
                