## 1995. Count Special Quadruplets

Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:

- nums[a] + nums[b] + nums[c] == nums[d], and
- a < b < c < d

### Example 1:

> Input: nums = [1,2,3,6]<br/>
> Output: 1<br/>
> Explanation: The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.

### Example 2:

> Input: nums = [3,3,6,4,5]<br/>
> Output: 0<br/>
> Explanation: There are no such quadruplets in [3,3,6,4,5].

### Example 3:

> Input: nums = [1,1,1,3,5]<br/>
> Output: 4<br/>
> Explanation: The 4 quadruplets that satisfy the requirement are:<br/>
> - (0, 1, 2, 3): 1 + 1 + 1 == 3
> - (0, 1, 3, 4): 1 + 1 + 3 == 5
> - (0, 2, 3, 4): 1 + 1 + 3 == 5
> - (1, 2, 3, 4): 1 + 1 + 3 == 5

### Constraints:

- 4 <= nums.length <= 50
- 1 <= nums[i] <= 100