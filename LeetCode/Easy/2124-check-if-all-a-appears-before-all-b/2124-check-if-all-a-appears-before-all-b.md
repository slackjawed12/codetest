## 2124. Check if All A's Appears Before All B's
Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.

### Example 1:

> Input: s = "aaabbb"<br/>
> Output: true<br/>
> Explanation:<br/>
> The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.<br/>
> Hence, every 'a' appears before every 'b' and we return true.

### Example 2:

> Input: s = "abab"<br/>
> Output: false<br/>
> Explanation:<br/>
> There is an 'a' at index 2 and a 'b' at index 1.<br/>
> Hence, not every 'a' appears before every 'b' and we return false.

### Example 3:

> Input: s = "bbb"<br/>
> Output: true<br/>
> Explanation:<br/>
> There are no 'a's, hence, every 'a' appears before every 'b' and we return true.
 
### Constraints:

- 1 <= s.length <= 100
- s[i] is either 'a' or 'b'.

### Topics

- String