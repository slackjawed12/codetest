## 2053. Kth Distinct String in an Array

A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.

### Example 1:

> Input: arr = ["d","b","c","b","c","a"], k = 2<br/>
> Output: "a"<br/>
> Explanation:<br/>
> The only distinct strings in arr are "d" and "a".<br/>
> "d" appears 1st, so it is the 1st distinct string.<br/>
> "a" appears 2nd, so it is the 2nd distinct string.<br/>
> Since k == 2, "a" is returned.<br/>

### Example 2:

> Input: arr = ["aaa","aa","a"], k = 1<br/>
> Output: "aaa"<br/>
> Explanation:<br>
> All strings in arr are distinct, so the 1st string "aaa" is returned.<br/>

### Example 3:

> Input: arr = ["a","b","a"], k = 3<br/>
> Output: ""<br/>
> Explanation:<br/>
> The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".

### Constraints:

- 1 <= k <= arr.length <= 1000
- 1 <= arr[i].length <= 5
- arr[i] consists of lowercase English letters.
