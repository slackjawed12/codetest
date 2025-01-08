# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1]*n for i in range(m)]
        i, j, d = 0,0,'r'
        while head:
            res[i][j] = head.val
            i, j, d = self.next_point(res, i, j, d)
            head = head.next
        
        return res
    
    def next_point(self, mat, i, j, d):
        if d == 'r':
            if j == len(mat[0])-1 or mat[i][j+1] != -1:
                return (i+1, j, 'd')
            else:
                return (i, j+1, d)
        elif d == 'd':
            if i == len(mat)-1 or mat[i+1][j] != -1:
                return (i, j-1, 'l')
            else:
                return (i+1, j, d)
        elif d == 'l':
            if j == 0 or mat[i][j-1] != -1:
                return (i-1, j, 'u')
            else:
                return (i, j-1, d)
        else:
            if i == 0 or mat[i-1][j] != -1:
                return (i, j+1, 'r')
            else:
                return (i-1, j, d)

            
            
        