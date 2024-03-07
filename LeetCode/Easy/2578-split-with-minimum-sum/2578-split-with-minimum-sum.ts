function splitNum(num: number): number {
  const numList = num.toString().split("");
  numList.sort();
  const num1 = parseInt(numList.filter((v, i) => i % 2 === 0).join(""));
  const num2 = parseInt(numList.filter((v, i) => i % 2 === 1).join(""));

  return num1 + num2;
}
