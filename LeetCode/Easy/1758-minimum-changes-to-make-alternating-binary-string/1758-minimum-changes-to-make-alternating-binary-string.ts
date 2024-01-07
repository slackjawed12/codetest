function minOperations(s: string): number {
  const unit = Math.floor(s.length / 2);
  const alternatings = ["01".repeat(unit), "10".repeat(unit)];
  if (s.length % 2 === 1) {
    alternatings[0] += "0";
    alternatings[1] += "1";
  }

  let answer = 99999;
  for (const alter of alternatings) {
    const listed = alter.split("");
    const diff = listed.reduce((prev, cur, index) => {
      if (cur !== s[index]) {
        prev += 1;
      }
      return prev;
    }, 0);
    answer = Math.min(diff, answer);
  }
  return answer;
}
