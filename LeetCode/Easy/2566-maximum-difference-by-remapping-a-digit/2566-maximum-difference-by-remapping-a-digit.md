## 2566. Maximum Difference by Remapping a Digit

You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.

Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.

### Notes:

- When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
- Bob can remap a digit to itself, in which case num does not change.
- Bob can remap different digits for obtaining minimum and maximum values respectively.
- The resulting number after remapping can contain leading zeroes.
 

### Example 1:

> Input: num = 11891<br/>
> Output: 99009<br/>
> Explanation: <br/>
> To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.<br/>
> To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.<br/>
> The difference between these two numbers is 99009.

### Example 2:

> Input: num = 90<br/>
> Output: 99<br/>
> Explanation:<br/>
> The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).<br/>
> Thus, we return 99.
 
### Constraints:

- `1 <= num <= 10^8`