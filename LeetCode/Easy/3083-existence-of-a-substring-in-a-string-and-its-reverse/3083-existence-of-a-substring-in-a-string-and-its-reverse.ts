function isSubstringPresent(s: string): boolean {
  const substrings = new Set();
  for (let i = 0; i < s.length - 1; i++) {
    substrings.add(s.slice(i, i + 2));
  }

  const reversed = s.split("").reverse().join("");
  for (let i = 0; i < reversed.length - 1; i++) {
    if (substrings.has(reversed.slice(i, i + 2))) {
      return true;
    }
  }

  return false;
}
