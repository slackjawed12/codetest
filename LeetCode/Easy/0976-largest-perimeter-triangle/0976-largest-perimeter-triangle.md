## 976. Largest Perimeter Triangle
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

### Example 1:

> Input: nums = [2,1,2]<br/>
> Output: 5<br/>
> Explanation: You can form a triangle with three side lengths: 1, 2, and 2.

### Example 2:

> Input: nums = [1,2,1,10]<br/>
> Output: 0<br/>
> Explanation: <br/>
> You cannot use the side lengths 1, 1, and 2 to form a triangle.<br/>
> You cannot use the side lengths 1, 1, and 10 to form a triangle.<br/>
> You cannot use the side lengths 1, 2, and 10 to form a triangle.<br/>
> As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
 
### Constraints:

- 3 <= nums.length <= 104
- 1 <= nums[i] <= 106

### Topics

- Array
- Math
- Greedy
- Sorting 