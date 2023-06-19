let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString();
//let input = fs.readFileSync('test.txt').toString();
let answer = [];
for(let i = 0; i<26; i++){
    answer[i]=0;
}

for(let i = 0; i<input.length; i++){
    answer[input[i].charCodeAt(0)-'a'.charCodeAt(0)]++;
}

answer.forEach(x=>process.stdout.write(x+' '))