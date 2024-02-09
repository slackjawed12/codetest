function makeSmallestPalindrome(s: string): string {
  const list = s.split("");
  const len = list.length;
  for (let i = 0; i < Math.floor(len / 2); i++) {
    if (list[i].charCodeAt(0) > list[len - i - 1].charCodeAt(0)) {
      list[i] = list[len - i - 1].slice();
    } else {
      list[len - i - 1] = list[i].slice();
    }
  }

  return list.join("");
}
