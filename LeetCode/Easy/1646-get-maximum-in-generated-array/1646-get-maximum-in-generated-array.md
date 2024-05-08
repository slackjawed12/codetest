## 1646. Get Maximum in Generated Array

You are given an integer n. A 0-indexed integer array nums of length n + 1 is generated in the following way:

- nums[0] = 0
- nums[1] = 1
- nums[2 * i] = nums[i] when 2 <= 2 * i <= n
- nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n

Return the maximum integer in the array nums​​​.

### Example 1:

> Input: n = 7<br/>
> Output: 3<br/>
> Explanation: According to the given rules:<br/>
>   nums[0] = 0<br/>
>   nums[1] = 1<br/>
>   nums[(1 * 2) = 2] = nums[1] = 1<br/>
>   nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2<br/>
>   nums[(2 * 2) = 4] = nums[2] = 1<br/>
>   nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3<br/>
>   nums[(3 * 2) = 6] = nums[3] = 2<br/>
>   nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3<br/>
> Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is max(0,1,1,2,1,3,2,3) = 3.

### Example 2:

> Input: n = 2<br/>
> Output: 1<br/>
> Explanation: According to the given rules, nums = [0,1,1]. The maximum is max(0,1,1) = 1.<br/>

### Example 3:

> Input: n = 3<br/>
> Output: 2<br/>
> Explanation: According to the given rules, nums = [0,1,1,2]. The maximum is max(0,1,1,2) = 2.<br/>
 
### Constraints:

- 0 <= n <= 100