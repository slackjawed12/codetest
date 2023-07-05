/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
    const result = moves.split("").reduce((prev,cur)=>{
        const x = prev.x + (cur === 'L' ? -1 : cur === 'R'? 1 : 0);
        const y = prev.y + (cur === 'D' ? -1 : cur === 'U'? 1 : 0);
        return {x, y}; 
    },{x:0, y:0})
    
    return result.x === 0 && result.y === 0;
};