class Solution:
    def validStrings(self, n: int) -> List[str]:
        dp = [None] * (n+1)
        dp[1] = ["0", "1"]
        for i in range(2, n+1):
            cur = []
            for c in dp[i-1]:
                cur.append(c + "1")
                if c[-1] == '1':
                    cur.append(c + "0")

            dp[i] = cur
                    
        return dp[n]
        