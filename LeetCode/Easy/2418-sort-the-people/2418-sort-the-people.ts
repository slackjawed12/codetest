function sortPeople(names: string[], heights: number[]): string[] {
  const formatted = names.map((v, i) => {
    return {
      name: v,
      height: heights[i],
    };
  });

  formatted.sort((o1, o2) => o2.height - o1.height);

  return formatted.map((v) => v.name);
}
