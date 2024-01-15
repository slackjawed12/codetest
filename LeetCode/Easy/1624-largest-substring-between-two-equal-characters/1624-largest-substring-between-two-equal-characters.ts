function maxLengthBetweenEqualCharacters(s: string): number {
  let maxLength = -1;
  for (let i = 0; i < s.length; i++) {
    for (let j = s.length - 1; j > i; j--) {
      if (s[j] === s[i]) {
        maxLength = Math.max(j - i - 1, maxLength);
        break;
      }
    }
  }
  return maxLength;
}
