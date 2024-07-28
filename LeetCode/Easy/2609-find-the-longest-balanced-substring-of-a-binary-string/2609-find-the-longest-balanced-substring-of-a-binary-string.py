class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        result = 0
        
        for i in range(0,len(s)):
            for j in range(i+1, len(s)):
                if (j-i+1) % 2 != 0:
                    continue
                
                sub = s[i:j+1]
                half_len = len(sub) // 2
                front, back = sub[:half_len], sub[half_len:]
                if front == '0'*(half_len) and back == '1'*(half_len):
                    result = max(len(sub), result)
            
        return result