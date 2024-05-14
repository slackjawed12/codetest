class Solution:
    def makeFancyString(self, s: str) -> str:
        arr = [s[0]]
        conti = 1
        for c in s[1:]:
           if arr[-1] == c:
               conti += 1
           else:
               conti = 1

           if conti >= 3:
               continue

           arr.append(c)
        
        return "".join(arr)
        