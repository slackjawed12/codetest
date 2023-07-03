/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function(jewels, stones) {
    return stones.split('').reduce((prev, cur)=> prev+=jewels.includes(cur),0);
};