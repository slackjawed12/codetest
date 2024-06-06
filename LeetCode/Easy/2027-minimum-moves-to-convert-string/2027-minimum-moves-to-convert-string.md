## 2027. Minimum Moves to Convert String
You are given a string s consisting of n characters which are either 'X' or 'O'.

A move is defined as selecting three consecutive characters of s and converting them to 'O'. Note that if a move is applied to the character 'O', it will stay the same.

Return the minimum number of moves required so that all the characters of s are converted to 'O'.

### Example 1:

> Input: s = "XXX"<br/>
> Output: 1<br/>
> Explanation: XXX -> OOO<br/>
> We select all the 3 characters and convert them in one move.

### Example 2:

> Input: s = "XXOX"<br/>
> Output: 2<br/>
> Explanation: XXOX -> OOOX -> OOOO<br/>
> We select the first 3 characters in the first move, and convert them to 'O'.<br/>
> Then we select the last 3 characters and convert them so that the final string contains all 'O's.

### Example 3:

> Input: s = "OOOO"<br/>
> Output: 0<br/>
> Explanation: There are no 'X's in s to convert.
 

### Constraints:

- 3 <= s.length <= 1000
- s[i] is either 'X' or 'O'.