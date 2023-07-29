/**
 * @param {number[]} position
 * @return {number}
 */
var minCostToMoveChips = function(position) {
  const counter = position.reduce((prev, cur)=>{
      const count = prev.get(cur);
      prev.set(cur, count ? count+1 : 1);
      return prev;
  }, new Map());

    const answer = Array.from(counter.keys()).reduce((prev, cur)=>{
        const ar = Array.from(counter);
        
        const cost = Array.from(counter)
        .reduce((acc,i)=>acc+=Math.abs(cur-i[0]) % 2 ? i[1] : 0, 0);
        return prev = Math.min(cost, prev);
    }, Infinity);
    
    return answer;
};