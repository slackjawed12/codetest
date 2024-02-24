function furthestDistanceFromOrigin(moves: string): number {
  const { left, right, underbar } = moves.split("").reduce(
    (prev, cur) => {
      if (cur === "L") {
        prev.left += 1;
      } else if (cur === "R") {
        prev.right += 1;
      } else {
        prev.underbar += 1;
      }
      return prev;
    },
    { left: 0, right: 0, underbar: 0 }
  );

  return Math.max(
    Math.abs(left + underbar - right),
    Math.abs(right + underbar - left)
  );
}
