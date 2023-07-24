/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicates = function(s) {
   return s.split("").reduce((prev, cur, i)=>{
       if(i===0) {
           prev.push(cur);
           return prev;
       }
       
       if(cur===prev[prev.length-1]){
           prev.pop();
           return prev;
       }
       
       prev.push(cur);
       return prev;
   }, []).join("");
};