function countSeniors(details: string[]): number {
  return details.reduce((prev, cur) => {
    const age = parseInt(cur[11] + cur[12]);
    prev += age > 60 ? 1 : 0;
    return prev;
  }, 0);
}
