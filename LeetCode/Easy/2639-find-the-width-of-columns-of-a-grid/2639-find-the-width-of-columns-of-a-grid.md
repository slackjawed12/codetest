## 2639. Find the Width of Columns of a Grid
You are given a 0-indexed m x n integer matrix grid. The width of a column is the maximum length of its integers.

For example, if grid = [[-10], [3], [12]], the width of the only column is 3 since -10 is of length 3.
Return an integer array ans of size n where ans[i] is the width of the ith column.

The length of an integer x with len digits is equal to len if x is non-negative, and len + 1 otherwise.

### Example 1:

> Input: grid = [[1],[22],[333]]<br/>
> Output: [3]<br/>
> Explanation: In the 0th column, 333 is of length 3.

### Example 2:

> Input: grid = [[-15,1,3],[15,7,12],[5,6,-2]]<br/>
> Output: [3,1,2]<br/>
> Explanation: <br/>
> In the 0th column, only -15 is of length 3.<br/>
> In the 1st column, all integers are of length 1.<br/> 
> In the 2nd column, both 12 and -2 are of length 2.<br/>

### Constraints:

_ m == grid.length
_ n == grid[i].length
_ 1 <= m, n <= 100 
_ -109 <= grid[r][c] <= 109