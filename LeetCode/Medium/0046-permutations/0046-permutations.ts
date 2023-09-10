function permute(nums: number[]): number[][] {
    return permuteHelper(nums, [], []);
};

function permuteHelper(nums: number[], current: number[], result: number[][]) {
    if(nums.length === 0) {
        result.push(current);
        return result;
    }
    
    let r;
    for(let i = 0; i < nums.length; i++) {
        const copiedCurrent = current.slice();
        copiedCurrent.push(nums[i]);
        const copy = nums.slice();
        copy.splice(i, 1);
        r = permuteHelper(copy, copiedCurrent, result);
    }
    
    return r;
}