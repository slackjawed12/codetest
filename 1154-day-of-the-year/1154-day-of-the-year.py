class Solution:
    def dayOfYear(self, date: str) -> int:
        days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
        y,m,d = [int(n) for n in date.split("-")]
        result = 0
        for c in range(m):
            result += days[c]
        
        result += d
        if m >= 3:
            if y % 4 == 0:
                if y % 100 != 0:
                    result += 1
                elif y % 400 == 0:
                    result += 1
            
        return result
        
           