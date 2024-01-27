function findMinimumOperations(s1: string, s2: string, s3: string): number {
  let start = 0;
  const minLength = Math.min(s1.length, s2.length, s3.length);
  while (
    start < minLength &&
    s1[start] === s2[start] &&
    s2[start] === s3[start]
  ) {
    start++;
  }

  return start === 0 ? -1 : s1.length + s2.length + s3.length - 3 * start;
}
