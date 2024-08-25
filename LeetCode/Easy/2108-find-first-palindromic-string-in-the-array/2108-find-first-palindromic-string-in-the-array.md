## 2108. Find First Palindromic String in the Array
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.

### Example 1:

> Input: words = ["abc","car","ada","racecar","cool"]<br/>
> Output: "ada"<br/>
> Explanation: The first string that is palindromic is "ada".<br/>
> Note that "racecar" is also palindromic, but it is not the first.

### Example 2:

> Input: words = ["notapalindrome","racecar"]<br/>
> Output: "racecar"<br/>
> Explanation: The first and only string that is palindromic is "racecar".

### Example 3:

> Input: words = ["def","ghi"]<br/>
> Output: ""<br/>
> Explanation: There are no palindromic strings, so the empty string is returned.
 

### Constraints:

- 1 <= words.length <= 100<br/>
- 1 <= words[i].length <= 100<br/>
- words[i] consists only of lowercase English letters.

### Topics

- Array
- Two Pointers
- String
