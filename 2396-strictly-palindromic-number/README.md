<h2><a href="https://leetcode.com/problems/strictly-palindromic-number">2396. Strictly Palindromic Number</a></h2><h3>Medium</h3><hr><p>An integer <code>n</code> is <strong>strictly palindromic</strong> if, for every base <code>b</code> between <code>2</code> and <code>n - 2</code> (inclusive), the string representation of the integer <code>n</code> in base <code>b</code> is palindromic.</p>

<p>Given an integer <code>n</code>, return <code>true</code> <em>if </em><code>n</code><em> is strictly palindromic and </em><code>false</code><em> otherwise.</em></p>

<p>A string is <em>palindromic</em> if it reads the same forward and backward.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 9
<strong>Output:</strong> false
<strong>Explanation:</strong> 9 in base 2 is 1001, which is palindromic.
In base 3, 9 is 100. It is not palindromic.
Therefore, 9 is not strictly palindromic so we return false.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> false
<strong>Explanation:</strong> In base 2, n = 100, which is not palindromic.
Therefore, 4 is not strictly palindromic so we return false.
</pre>


<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>4 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>