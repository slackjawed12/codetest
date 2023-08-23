function findNumbers(nums: number[]): number {
    return nums.filter(v=>!(v.toString().length %2)).length;
};