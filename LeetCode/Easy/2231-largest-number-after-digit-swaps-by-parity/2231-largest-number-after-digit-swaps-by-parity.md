## 2231. Largest Number After Digit Swaps by Parity
You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps.

### Example 1:

> Input: num = 1234<br/>
> Output: 3412<br/>
> Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.<br/>
> Swap the digit 2 with the digit 4, this results in the number 3412.<br/>
> Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.<br/>
> Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.

### Example 2:

> Input: num = 65875<br/>
> Output: 87655<br/>
> Explanation: Swap the digit 8 with the digit 6, this results in the number 85675.<br/>
> Swap the first digit 5 with the digit 7, this results in the number 87655.<br/>
> Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.
 
### Constraints:

- 1 <= num <= 109

### Topics

- Sorting
- Heap (Priority Queue)