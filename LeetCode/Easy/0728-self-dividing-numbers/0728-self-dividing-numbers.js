/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var selfDividingNumbers = function(left, right) {
    return Array.from(Array(right-left+1), (_,i)=>i+left)
        .filter((val)=>{
            return val.toString()
                        .split("")
                        .map(Number)
                        .every((digit)=>digit!==0 && !(val%digit));
    });
};