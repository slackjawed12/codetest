function numIdenticalPairs(nums: number[]): number {
    let result =0;
    for(let i=0; i<nums.length-1; i++){
        for(let j=i+1; j<nums.length; j++){
            result = result + +(nums[i]===nums[j])
        }
    }
    
    return result;
};