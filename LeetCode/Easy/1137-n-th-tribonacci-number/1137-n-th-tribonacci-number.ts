function tribonacci(n: number): number {
    const dp = [0,1,1, ...Array(Math.max(0, n-2))];
    for(let i=3; i<=n; i++){
        dp[i]=dp[i-3]+dp[i-2]+dp[i-1];
    }
    return dp[n];
};