function maximumPopulation(logs: number[][]): number {
  logs.sort((o1, o2) => o1[0] - o2[0]);
  return logs.reduce(
    (prev, cur) => {
      const living = logs.filter((l) => l[1] > cur[0] && l[0] <= cur[0]).length;
      if (living > prev[0]) {
        return [living, cur[0]];
      }
      return prev;
    },
    [0, 0]
  )[1];
}
