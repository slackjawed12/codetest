## 2283. Check if Number Has Equal Digit Count and Digit Value
You are given a 0-indexed string num of length n consisting of digits.

Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, otherwise return false.

### Example 1:

> Input: num = "1210"<br/>
> Output: true<br/>
> Explanation:<br/>
> num[0] = '1'. The digit 0 occurs once in num.<br/>
> num[1] = '2'. The digit 1 occurs twice in num.<br/>
> num[2] = '1'. The digit 2 occurs once in num.<br/>
> num[3] = '0'. The digit 3 occurs zero times in num.<br/>
> The condition holds true for every index in "1210", so return true.

### Example 2:

> Input: num = "030"<br/>
> Output: false<br/>
> Explanation:<br/>
> num[0] = '0'. The digit 0 should occur zero times, but actually occurs twice in num.<br/>
> num[1] = '3'. The digit 1 should occur three times, but actually occurs zero times in num.<br/>
> num[2] = '0'. The digit 2 occurs zero times in num.<br/>
> The indices 0 and 1 both violate the condition, so return false.<br/>

### Constraints:

- n == num.length
- 1 <= n <= 10
- num consists of digits.