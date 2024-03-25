function sumOfEncryptedInt(nums: number[]): number {
  const encrypt = (num: number) => {
    const digits = num
      .toString()
      .split("")
      .map((c) => parseInt(c));
    const maxDigit = digits.reduce((prev, cur) => Math.max(prev, cur), 0);
    return parseInt(digits.map((num) => maxDigit).join(""));
  };

  return nums.map((n) => encrypt(n)).reduce((acc, cur) => (acc += cur), 0);
}
