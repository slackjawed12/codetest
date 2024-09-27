## 697. Degree of an Array
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

### Example 1:

> Input: nums = [1,2,2,3,1]<br/>
> Output: 2<br/>
> Explanation: <br/>
> The input array has a degree of 2 because both elements 1 and 2 appear twice.<br/>
> Of the subarrays that have the same degree:<br/>
> [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]<br/>
> The shortest length is 2. So return 2.

### Example 2:

> Input: nums = [1,2,2,3,1,4,2]<br/>
> Output: 6<br/>
> Explanation: <br/>
> The degree is 3 because the element 2 is repeated 3 times.<br/>
> So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
 

### Constraints:

- nums.length will be between 1 and 50,000.
- nums[i] will be an integer between 0 and 49,999.

### Topics

- Array
- Hash Table