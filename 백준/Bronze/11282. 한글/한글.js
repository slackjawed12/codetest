let fs = require('fs');
let input = +fs.readFileSync('/dev/stdin').toString().split();
let answer=String.fromCharCode('가'.charCodeAt(0)+input-1);

console.log(answer);