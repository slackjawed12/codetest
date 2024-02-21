## 2815. Max Pair Sum in an Array

You are given a 0-indexed integer array nums. You have to find the maximum sum of a pair of numbers from nums such that the maximum digit in both numbers are equal.

Return the maximum sum or -1 if no such pair exists.

### Example 1:

> Input: nums = [51,71,17,24,42]</br>
> Output: 88</br>
> Explanation:</br>
> For i = 1 and j = 2, nums[i] and nums[j] have equal maximum digits with a pair sum of 71 + 17 = 88.</br>
> For i = 3 and j = 4, nums[i] and nums[j] have equal maximum digits with a pair sum of 24 + 42 = 66.</br>
> It can be shown that there are no other pairs with equal maximum digits, so the answer is 88.

### Example 2:

> Input: nums = [1,2,3,4]</br>
> Output: -1</br>
> Explanation: No pair exists in nums with equal maximum digits.</br>

### Constraints:

- 2 <= nums.length <= 100
- 1 <= nums[i] <= 10^4
