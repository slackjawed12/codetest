## 2595. Number of Even and Odd Bits

You are given a positive integer n.

Let even denote the number of even indices in the binary representation of n (0-indexed) with value 1.

Let odd denote the number of odd indices in the binary representation of n (0-indexed) with value 1.

Return an integer array answer where answer = [even, odd].

### Example 1:

> Input: n = 17<br/>
> Output: [2,0]<br/>
> Explanation: The binary representation of 17 is 10001.<br/>
> It contains 1 on the 0th and 4th indices.<br/>
> There are 2 even and 0 odd indices.

### Example 2:

> Input: n = 2<br/>
> Output: [0,1]<br/>
> Explanation: The binary representation of 2 is 10.<br/>
> It contains 1 on the 1st index.<br/>
> There are 0 even and 1 odd indices.

### Constraints:

- 1 <= n <= 1000
