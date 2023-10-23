function minStartValue(nums: number[]): number {
    const cumulative = nums.reduce((prev,cur, index)=>{
        prev[index] += index === 0 ? 0 : prev[index-1];
        return prev;
    },nums);
    
    const min = Math.min(...cumulative);
    
    return min > 0 ? 1 : Math.abs(min-1);
};