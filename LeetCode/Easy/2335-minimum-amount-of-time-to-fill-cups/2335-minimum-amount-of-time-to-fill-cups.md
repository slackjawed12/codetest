## 2335. Minimum Amount of Time to Fill Cups
You have a water dispenser that can dispense cold, warm, and hot water. Every second, you can either fill up 2 cups with different types of water, or 1 cup of any type of water.

You are given a 0-indexed integer array amount of length 3 where amount[0], amount[1], and amount[2] denote the number of cold, warm, and hot water cups you need to fill respectively. Return the minimum number of seconds needed to fill up all the cups.

### Example 1:

> Input: amount = [1,4,2]<br/>
> Output: 4<br/>
> Explanation: One way to fill up the cups is:<br/>
> Second 1: Fill up a cold cup and a warm cup.<br/>
> Second 2: Fill up a warm cup and a hot cup.<br/>
> Second 3: Fill up a warm cup and a hot cup.<br/>
> Second 4: Fill up a warm cup.<br/>
> It can be proven that 4 is the minimum number of seconds needed.

### Example 2:

> Input: amount = [5,4,4]<br/>
> Output: 7<br/>
> Explanation: One way to fill up the cups is:<br/>
> Second 1: Fill up a cold cup, and a hot cup.<br/>
> Second 2: Fill up a cold cup, and a warm cup.<br/>
> Second 3: Fill up a cold cup, and a warm cup.<br/>
> Second 4: Fill up a warm cup, and a hot cup.<br/>
> Second 5: Fill up a cold cup, and a hot cup.<br/>
> Second 6: Fill up a cold cup, and a warm cup.<br/>
> Second 7: Fill up a hot cup.

### Example 3:

> Input: amount = [5,0,0]<br/>
> Output: 5<br/>
> Explanation: Every second, we fill up a cold cup.

### Constraints:

- amount.length == 3
- 0 <= amount[i] <= 100