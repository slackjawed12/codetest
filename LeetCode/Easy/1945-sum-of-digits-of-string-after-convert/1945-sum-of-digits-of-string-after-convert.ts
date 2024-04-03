function getLucky(s: string, k: number): number {
  const toCharCodeString = (c: string) => {
    return (c.charCodeAt(0) - "a".charCodeAt(0) + 1).toString();
  };

  const stringList = s.split("");
  const converted = BigInt(stringList.map((c) => toCharCodeString(c)).join(""));
  let result = converted;
  for (let i = 1; i <= k; i++) {
    let temp = 0n;
    while (result > 0) {
      temp += result % 10n;
      result = result / 10n;
    }
    result = temp;
  }

  return Number(result);
}
