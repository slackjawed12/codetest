class Solution:
    def isBalanced(self, num: str) -> bool:
        e, o =0,0
        for i in range(len(num)):
            if i % 2:
                o += int(num[i])
            else:
                e += int(num[i])
        
        return e == o