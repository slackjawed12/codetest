/**
 * @param {string[]} list1
 * @param {string[]} list2
 * @return {string[]}
 */
var findRestaurant = function(list1, list2) {
    let set = {};
    for (const [i, str] of list1.entries()) {
        set[str] = i;
    }
    
    let least = Infinity;
    let answer = [];
    for(const [i, str] of list2.entries()){
        if(set.hasOwnProperty(str)) {
            if(set[str] + i < least) {
                least = set[str] + i;
                answer =[];
                answer.push(str);
            } else if(set[str] + i === least) {
                answer.push(str);
            }
        }
    }
    return answer;
};