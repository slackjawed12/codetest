function minTimeToType(word: string): number {
  const minDistance = (a: string, b: string) => {
    const [max, min] = [
      Math.max(a.charCodeAt(0), b.charCodeAt(0)),
      Math.min(a.charCodeAt(0), b.charCodeAt(0)),
    ];
    const clockwiseDistance = min + 26 - max;
    const counterClockwiseDistance = max - min;
    return Math.min(clockwiseDistance, counterClockwiseDistance);
  };

  return word.split("").reduce(
    (prev, cur, index) => {
      if (cur !== prev.pointer) {
        return {
          second: prev.second + 1 + minDistance(cur, prev.pointer),
          pointer: cur,
        };
      }

      return {
        second: prev.second + 1,
        pointer: cur,
      };
    },
    { second: 0, pointer: "a" }
  ).second;
}
