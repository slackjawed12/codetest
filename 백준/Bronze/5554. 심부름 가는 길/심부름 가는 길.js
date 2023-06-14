let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
// let input = fs.readFileSync('test.txt').toString().split('\n');
let answer = [];
let total = 0;
for (const i of input) {
    total += +i;
}
let m = Math.floor(total / 60);
let s = total % 60;
answer.push(m);
answer.push(s);

for (let i = 0; i < answer.length; i++) {
    console.log(answer[i]);
}