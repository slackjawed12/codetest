/**
 * @param {string} s
 * @return {number[]}
 */
var diStringMatch = function(s) {
    const arr = Array.from(Array(s.length+1), (_,i)=>i);
    
    const answer = s.split("").reduce((prev, cur)=>{
        if(cur==='I') {
            prev.push(arr.shift());
        } else {
            prev.push(arr.pop());
        }
        return prev;
    }, []);
    
    answer.push(arr.pop());
    
    return answer;
};