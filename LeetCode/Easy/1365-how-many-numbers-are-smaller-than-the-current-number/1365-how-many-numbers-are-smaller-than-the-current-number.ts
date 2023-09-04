function smallerNumbersThanCurrent(nums: number[]): number[] {
    const mapped = nums.map((val, i)=>{
        const temp = nums.reduce((acc,cur,j)=>{
            if(j!=i && cur<val) {
                acc++;
            }
            return acc;
        }, 0);
        return temp;
    })
    
    return mapped;
};