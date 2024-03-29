function maximumLengthSubstring(s: string): number {
  let answer = 0;
  for (let i = 0; i < s.length - 1; i++) {
    for (let j = i; j < s.length; j++) {
      const sublist = s.slice(i, j + 1).split("");
      const store = sublist.reduce((prev, cur) => {
        const count = prev.get(cur);
        prev.set(cur, count ? count + 1 : 1);
        return prev;
      }, new Map());
      const valueList = Array.from(store).map((entry) => entry[1]);
      const maxCount = valueList.reduce((acc, cur) => Math.max(acc, cur), 0);
      if (maxCount <= 2) {
        answer = Math.max(sublist.length, answer);
      }
    }
  }

  return answer;
}
