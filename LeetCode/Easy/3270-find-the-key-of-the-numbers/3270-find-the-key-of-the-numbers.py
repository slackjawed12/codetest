class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        ss = [str(num1), str(num2), str(num3)]
        pad = ["0"*(4-len(n))+n for n in ss]
        result = ""
        for i in range(4):
            m = 9
            for p in pad:
                m = min(int(p[i]), m)
            
            result += str(m)
            
        return int(result)