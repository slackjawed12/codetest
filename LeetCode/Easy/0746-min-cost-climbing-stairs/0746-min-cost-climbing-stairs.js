/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(cost) {
    const dp = cost.reduce((acc,cur)=>{
        const costOneStep = acc[acc.length-1]+cur;
        const costTwoStep = acc[Math.max(0,acc.length-2)]+cur;
        acc.push(Math.min(costOneStep, costTwoStep));
        return acc;
    },[0]);
    
    return Math.min(dp[cost.length], dp[cost.length-1]);
};