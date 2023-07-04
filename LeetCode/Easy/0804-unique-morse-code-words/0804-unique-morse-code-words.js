/**
 * @param {string[]} words
 * @return {number}
 */
var uniqueMorseRepresentations = function(words) {
    const morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."].reduce((prev, cur, index) => {
        const key = String.fromCharCode(index+97);
        return {...prev, [key]:cur};
    }, {});

    const obj =  words.reduce((prev, cur) => {
        const code = cur.split("").reduce((prev,cur)=>prev.concat(morse[cur]),"");
        return {...prev, [code]:0};
    }, {});
    
    return Object.keys(obj).length;
};