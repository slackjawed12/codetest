/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} ops
 * @return {number}
 */
var maxCount = function(m, n, ops) {
    let mx = m;
    let my = n;
    for (const position of ops){
        mx = Math.min(mx, position[0]);
        my = Math.min(my, position[1]);
    }
    
    return mx*my;
};