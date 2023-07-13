/**
 * @param {number[][]} matrix
 * @return {boolean}
 */
var isToeplitzMatrix = function(matrix) {
    const result = matrix.slice(1).reduce((prev, cur)=>{
        return [...cur.slice(0,-1), 
                prev[prev.length-1] && cur.slice(1).every((val, i) => prev[i]===val)];
    }, [...matrix[0].slice(0,-1), true]);
    return result[result.length-1];
};