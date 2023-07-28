/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
    const occurCounts = arr.reduce((prev, cur)=>{
        const before = prev.get(cur);
        prev.set(cur, !before?1:(before+1));
        
        return prev;
    },new Map());
    
    const set = new Set(occurCounts.values());
    
    return set.size===occurCounts.size;
};