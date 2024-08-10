## 2287. Rearrange Characters to Make Target String
You are given two 0-indexed strings s and target. You can take some letters from s and rearrange them to form new strings.

Return the maximum number of copies of target that can be formed by taking letters from s and rearranging them.

### Example 1:

> Input: s = "ilovecodingonleetcode", target = "code"<br/>
> Output: 2<br/>
> Explanation:<br/>
> For the first copy of "code", take the letters at indices 4, 5, 6, and 7.<br/>
> For the second copy of "code", take the letters at indices 17, 18, 19, and 20.<br/>
> The strings that are formed are "ecod" and "code" which can both be rearranged into "code".<br/>
> We can make at most two copies of "code", so we return 2.

### Example 2:

> Input: s = "abcba", target = "abc"<br/>
> Output: 1<br/>
> Explanation:<br/>
> We can make one copy of "abc" by taking the letters at indices 0, 1, and 2.<br/>
> We can make at most one copy of "abc", so we return 1.<br/>
> Note that while there is an extra 'a' and 'b' at indices 3 and 4, we cannot reuse the letter 'c' at index 2, so we cannot make a second copy of "abc".<br/>

### Example 3:

> Input: s = "abbaccaddaeea", target = "aaaaa"<br/>
> Output: 1<br/>
> Explanation:<br/>
> We can make one copy of "aaaaa" by taking the letters at indices 0, 3, 6, 9, and 12.<br/>
> We can make at most one copy of "aaaaa", so we return 1.
 
### Constraints:

- 1 <= s.length <= 100
- 1 <= target.length <= 10
- s and target consist of lowercase English letters.

### Topics

- Hash Table
- String
- Counting
