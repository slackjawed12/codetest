/**
 * @param {number[]} nums
 * @return {number}
 */
var findLengthOfLCIS = function(nums) {
    const answer = nums.reduce((acc, cur, i, nums)=>{
        if(i===0) {
            acc.push(1);
            return acc;
        }
        
        acc.push(cur>nums[i-1]?acc[acc.length-1]+1:1);
        return acc;
    }, [])
    
    return Math.max(...answer);
};