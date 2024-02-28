function minLength(s: string): number {
  let temp = s;

  while (temp.includes("AB") || temp.includes("CD")) {
    for (let i = 0; i < temp.length - 1; i++) {
      if (temp[i] === "A" && temp[i + 1] === "B") {
        temp = temp.slice(0, i) + temp.slice(i + 2);
      } else if (temp[i] === "C" && temp[i + 1] === "D") {
        temp = temp.slice(0, i) + temp.slice(i + 2);
      }
    }
  }

  return temp.length;
}
