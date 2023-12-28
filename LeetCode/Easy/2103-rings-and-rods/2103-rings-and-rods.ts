function countPoints(rings: string): number {
  const ringsList = rings.split("");
  const info = ringsList.reduce(
    (prev, cur, index) => {
      if (index % 2 === 1) {
        const [color, rod] = [ringsList[index - 1], parseInt(cur)];
        prev[rod][color] += 1;
        return prev;
      }

      return prev;
    },
    Array.from(Array(10), (_) => ({ R: 0, G: 0, B: 0 }))
  );

  return info.filter((v) => v.R >= 1 && v.G >= 1 && v.B >= 1).length;
}
