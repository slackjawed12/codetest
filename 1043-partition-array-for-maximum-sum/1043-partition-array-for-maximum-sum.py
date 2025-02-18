class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr)+1)
        for i in range(1, len(arr)+1):
            for j in range(1, k+1):
                if j > i:
                    continue
                
                submax = max(arr[i-j:i])
                dp[i] = max(dp[i], dp[i-j] + submax * j)
        
        return dp[len(arr)]
