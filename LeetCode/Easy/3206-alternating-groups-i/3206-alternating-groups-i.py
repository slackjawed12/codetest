class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        result =0
        for i in range(len(colors)):
            a,b,c= colors[i-1], colors[i], colors[(i+1)%len(colors)]
            if a != b and b != c:
                result+=1
        
        return result