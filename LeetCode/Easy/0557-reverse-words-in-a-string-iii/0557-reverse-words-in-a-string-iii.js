/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    console.log(s);
    const input = s.split(' ');
    let answer = '';
    
    for(const word of input){
        for(let j=word.length-1; j>=0; j--){
            answer += word[j];   
        }
        answer += ' ';
    }
    
    return answer.trimEnd();
};