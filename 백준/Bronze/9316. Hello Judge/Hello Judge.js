let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split();
let answer = [];

for (let i = 1; i <= parseInt(input); i++) {
    answer.push('Hello World, Judge ' + i + '!');
}

answer.forEach(x => console.log(x));