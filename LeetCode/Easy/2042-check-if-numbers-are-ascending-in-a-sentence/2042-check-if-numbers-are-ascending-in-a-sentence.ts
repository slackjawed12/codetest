function areNumbersAscending(s: string): boolean {
  const reg = /[0-9]+/;
  let cur = 0;
  const words = s.split(" ");
  for (const word of words) {
    const isNumeral = reg.test(word);
    if (!isNumeral) {
      continue;
    }

    if (cur >= parseInt(word)) {
      return false;
    }

    cur = parseInt(word);
  }

  return true;
}
