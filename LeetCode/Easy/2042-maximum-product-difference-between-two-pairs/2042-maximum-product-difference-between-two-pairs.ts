function maxProductDifference(nums: number[]): number {
    nums.sort((o1,o2)=>o2-o1)
    return (nums[0]*nums[1]-nums[nums.length-1]*nums[nums.length-2])
};