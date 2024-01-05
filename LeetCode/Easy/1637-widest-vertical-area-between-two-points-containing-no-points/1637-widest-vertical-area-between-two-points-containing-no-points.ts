function maxWidthOfVerticalArea(points: number[][]): number {
  points.sort((o1, o2) => o1[0] - o2[0]);
  return points.slice(1).reduce(
    (prev, cur) => {
      return [Math.max(prev[0], cur[0] - prev[1]), cur[0]];
    },
    [0, points[0][0]]
  )[0];
}
