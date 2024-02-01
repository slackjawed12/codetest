function maximumOddBinaryNumber(s: string): string {
  let zero = 0;
  let one = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === "0") {
      zero += 1;
    } else {
      one += 1;
    }
  }

  return "1".repeat(one - 1) + "0".repeat(zero) + "1";
}
