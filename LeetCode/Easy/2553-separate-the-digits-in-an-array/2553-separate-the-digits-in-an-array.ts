function separateDigits(nums: number[]): number[] {
  const answer = nums.reduce<number[]>((prev, cur) => {
    return [
      ...prev,
      ...cur
        .toString()
        .split("")
        .map((d) => parseInt(d)),
    ];
  }, []);
  return answer;
}
