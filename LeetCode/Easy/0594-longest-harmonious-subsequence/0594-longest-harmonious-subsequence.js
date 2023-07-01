/**
 * @param {number[]} nums
 * @return {number}
 */
var findLHS = function(nums) {
    let counter = {};
    for(const num of nums){
        counter[num] = 1+(counter[num] ?? 0);
    }
    
    let answer = 0;
    for(const i in counter){
        const next = (parseInt(i)+1).toString();
        if(next in counter){
            answer = Math.max(answer, counter[next]+counter[i]);
        }
    }
    return answer;
};