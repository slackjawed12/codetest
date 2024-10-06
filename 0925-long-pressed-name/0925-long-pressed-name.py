class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i,j = 0,0
        x,y = 1,0
        while i < len(name):
            if i==0 or (i != 0 and name[i-1] != name[i]):
                x,y = 1, 0
                while j != len(typed) and name[i] == typed[j]:
                    j += 1
                    y += 1
            else:
                x += 1
                
            if x > y:
                return False
            i += 1
        
        return j == len(typed)