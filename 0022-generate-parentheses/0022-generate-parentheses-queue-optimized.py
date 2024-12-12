class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp =[None]*(n+1)
        dp[1] = set(["()"])
        for i in range(2,n+1):
            dp[i] = set()
            for j in range(1, i):
                for b in dp[j]:
                    if j == i-1:
                        dp[i].add("("+b+")")
                    for c in dp[i-j]:
                        dp[i].add(b+c)
        
        return list(dp[n])