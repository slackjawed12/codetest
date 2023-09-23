function maxProduct(nums: number[]): number {
    const first = nums.reduce((prev,cur)=>{
        return Math.max(prev,cur)
    }, 0);
    
    const idx = nums.findIndex(x=>x===first);
    nums.splice(idx, 1);
    const second =nums.reduce((prev,cur)=>Math.max(prev,cur), 0)
    
    return (first-1)*(second-1);
};