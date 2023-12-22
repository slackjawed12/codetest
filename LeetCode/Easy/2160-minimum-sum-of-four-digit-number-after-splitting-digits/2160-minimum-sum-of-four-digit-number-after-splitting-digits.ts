function minimumSum(num: number): number {
  const converted = num
    .toString()
    .split("")
    .map((i) => parseInt(i));
  converted.sort((o1, o2) => o1 - o2);

  return (
    parseInt(converted[0].toString() + converted[3].toString()) +
    parseInt(converted[1].toString() + converted[2].toString())
  );
}
