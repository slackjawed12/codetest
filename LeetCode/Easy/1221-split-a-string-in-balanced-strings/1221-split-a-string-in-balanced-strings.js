/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function(s) {
    let l=0;
    let r=0;
    let answer = 0;
    for(let i=0; i<s.length; i++){
        if(s[i]==='L') {
            l++;
        } else {
            r++;
        }
        
        if(l === r){
            l =0;
            r=0;
            answer++;
        }
    }
    
    return answer;
};