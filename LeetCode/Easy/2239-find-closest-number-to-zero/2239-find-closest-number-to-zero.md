## 2239. Find Closest Number to Zero
Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

### Example 1:

> Input: nums = [-4,-2,1,4,8]<br/>
> Output: 1<br/>
> Explanation:<br/>
> The distance from -4 to 0 is |-4| = 4.<br/>
> The distance from -2 to 0 is |-2| = 2.<br/>
> The distance from 1 to 0 is |1| = 1.<br/>
> The distance from 4 to 0 is |4| = 4.<br/>
> The distance from 8 to 0 is |8| = 8.<br/>
> Thus, the closest number to 0 in the array is 1.

### Example 2:

> Input: nums = [2,-1,1]<br/>
> Output: 1<br/>
> Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
 
### Constraints:

- 1 <= n <= 1000
- -105 <= nums[i] <= 105

### Topics

- Array