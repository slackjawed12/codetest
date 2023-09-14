function runningSum(nums: number[]): number[] {
    return nums.reduce((prev,cur)=>{
        if(prev.length===0) {
            prev.push(cur)    
        } else {
            prev.push(prev[prev.length-1] + cur);
        }
        return prev;
    },[])
};