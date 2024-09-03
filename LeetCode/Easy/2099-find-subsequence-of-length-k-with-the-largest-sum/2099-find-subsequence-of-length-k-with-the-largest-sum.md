## 2099. Find Subsequence of Length K With the Largest Sum
You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

### Example 1:

> Input: nums = [2,1,3,3], k = 2<br/>
> Output: [3,3]<br/>
> Explanation:<br/>
> The subsequence has the largest sum of 3 + 3 = 6.

### Example 2:

> Input: nums = [-1,-2,3,4], k = 3<br/>
> Output: [-1,3,4]<br/>
> Explanation: <br/>
> The subsequence has the largest sum of -1 + 3 + 4 = 6.

### Example 3:

> Input: nums = [3,4,3,3], k = 2<br/>
> Output: [3,4]<br/>
> Explanation:<br/>
> The subsequence has the largest sum of 3 + 4 = 7. <br/>
> Another possible subsequence is [4, 3].
 
### Constraints:

- 1 <= nums.length <= 1000
- -105 <= nums[i] <= 105
- 1 <= k <= nums.length

### Topics

- Array
- Hash Table
- Sorting
- Heap (Priority Queue)