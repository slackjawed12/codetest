function reversePrefix(word: string, ch: string): string {
  const index = word.indexOf(ch);
  console.log(index);
  if (index === -1) {
    return word;
  }

  const reverse = (s: string) => {
    let result: string[] = [];
    for (let i = s.length - 1; i >= 0; i--) {
      result.push(s[i]);
    }
    return result.join("");
  };

  const prefix = reverse(word.slice(0, index + 1));
  const sliced = word.slice(index + 1);
  return prefix + sliced;
}
