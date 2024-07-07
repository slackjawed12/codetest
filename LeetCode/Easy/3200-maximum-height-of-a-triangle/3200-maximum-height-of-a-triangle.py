class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        result_b = self.height(blue, red, 'b')
        result_r = self.height(blue, red, 'r')
        return max(result_b, result_r)
    
    def height(self, blue:int, red:int, first:str)->int:
        d = {"b":blue, "r":red}
        second = 'b' if first == 'r' else 'r'
        cnt, flag = 1, True
        result = 0
        while True:
            c = first if flag else second
            if d[c] >= cnt:
                d[c] -= cnt
                flag = not flag
                cnt += 1
                result += 1
            else:
                break

        return result