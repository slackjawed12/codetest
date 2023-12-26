// runtime 5.13%, memory 5.13%
function areAlmostEqual(s1: string, s2: string): boolean {
  let temp = s2.split("");
  for (let i = 0; i < s2.length; i++) {
    for (let j = 0; j < s2.length; j++) {
      temp[i] = s2[j];
      temp[j] = s2[i];
      if (s1 === temp.join("")) {
        return true;
      }
      temp[i] = s2[i];
      temp[j] = s2[j];
    }
  }
  return false;
}

// runtime 89.74%, memory 41.03%
function areAlmostEqualV2(s1: string, s2: string): boolean {
  if (s1.split("").sort().join("") === s2.split("").sort().join("")) {
    let count = 0;
    for (let i = 0; i < s1.length; i++) {
      if (s1[i] !== s2[i]) {
        count++;
        if (count > 2) {
          return false;
        }
      }
    }
    return true;
  }
  return false;
}
