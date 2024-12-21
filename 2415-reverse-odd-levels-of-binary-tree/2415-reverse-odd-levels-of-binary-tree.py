# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        
        q = deque([])
        q.append((root, 0))
        while q:
            cur, lev = q.popleft()
            if cur is None:
                continue
                
            q.append((cur.left, lev+1))
            q.append((cur.right, lev+1))

            if lev % 2 != 0:
                odds = [cur]
                while q and q[0][1] == lev:
                    q.append((q[0][0].left, lev+1))
                    q.append((q[0][0].right, lev+1))
                    odds.append(q.popleft()[0])
                
                for i in range(len(odds)//2):
                    odds[i].val, odds[len(odds)-i-1].val = odds[len(odds)-i-1].val, odds[i].val

        return root