function numberOfPoints(nums: number[][]): number {
  nums.sort((o1, o2) => -o1[1] + o2[1]);
  let start = 101;
  let answer = 0;
  for (const num of nums) {
    const [s, e] = num;
    if (e < start) {
      // out
      answer += e - s + 1;
      start = s;
    } else if (s < start) {
      // overlap
      answer += start - s;
      start = s;
    }
  }

  return answer;
}
