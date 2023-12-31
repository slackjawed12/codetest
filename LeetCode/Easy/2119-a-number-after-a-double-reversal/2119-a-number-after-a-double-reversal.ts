function isSameAfterReversals(num: number): boolean {
  let temp = num;
  let reversed1 = 0;
  while (temp != 0) {
    reversed1 *= 10;
    reversed1 += temp % 10;
    temp = Math.floor(temp / 10);
  }

  let reversed2 = 0;
  temp = reversed1;
  while (temp != 0) {
    reversed2 *= 10;
    reversed2 += temp % 10;
    temp = Math.floor(temp / 10);
  }
  return num === reversed2;
}

// simple solution
function isSameAfterReversalsV2(num: number): boolean {
  return num === 0 || !(num % 10 === 0);
}
