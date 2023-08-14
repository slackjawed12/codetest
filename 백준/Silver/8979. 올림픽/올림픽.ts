import fs = require("fs");

const [inputs, ...medals] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [N, K] = inputs.split(" ").map(Number);
const info = medals.map((row) => row.split(" ").map(Number));

info.sort((r1, r2) => {
  if (r1[1] !== r2[1]) {
    return r2[1] - r1[1];
  } else if (r1[2] !== r2[2]) {
    return r2[2] - r1[2];
  } else if (r1[3] !== r2[3]) {
    return r2[3] - r1[3];
  } else {
    return 0;
  }
});

let rank = 1;
for (let i = 0; i < info.length; i++) {
  if (info[i][0] === K || i === info.length - 1) {
    console.log(rank);
    break;
  }

  if (
    info[i][1] !== info[i + 1][1] ||
    info[i][2] !== info[i + 1][2] ||
    info[i][3] !== info[i + 1][3]
  ) {
    rank = i + 2;
  }
}
