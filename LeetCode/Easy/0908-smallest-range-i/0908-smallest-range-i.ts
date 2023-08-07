function smallestRangeI(nums: number[], k: number): number {
    nums.sort((x,y)=>x-y);
    const diff = nums[nums.length-1]-nums[0];
    if(diff > 2 * k) {
        return diff-2*k;
    } else {
        return 0;
    }
};