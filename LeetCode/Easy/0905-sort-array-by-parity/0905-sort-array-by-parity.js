/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParity = function(nums) {
    return nums.filter(n=>!(n%2)).concat(nums.filter(n=>n%2));
};