function finalString(s: string): string {
  const answer = s.split("").reduce((prev, cur) => {
    if (cur === "i") {
      return Array.from(prev).reverse().join("");
    }

    return prev + cur;
  }, "");
  return answer;
}
