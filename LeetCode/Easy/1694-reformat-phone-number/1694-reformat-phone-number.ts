function reformatNumber(number: string): string {
  const onlyDigits = number.replace(/[\\-\s]/g, "");
  const arr: string[] = [];
  let i = 0;
  while (i < onlyDigits.length) {
    const rem = onlyDigits.length - i;
    if (rem <= 3) {
      arr.push(onlyDigits.slice(i));
      i += rem;
    } else if (rem === 4) {
      arr.push(onlyDigits.slice(i, i + 2));
      arr.push("-");
      i += 2;
    } else {
      arr.push(onlyDigits.slice(i, i + 3));
      arr.push("-");
      i += 3;
    }
  }
  return arr.join("");
}
