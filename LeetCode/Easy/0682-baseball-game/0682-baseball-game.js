/**
 * @param {string[]} operations
 * @return {number}
 */
var calPoints = function(operations) {
    return operations.reduce((prev,cur)=>{
        switch(cur){
            case 'C':
                prev.pop();
                break;
            case 'D':
                prev.push(prev[prev.length-1]*2);
                break;
            case '+':
                prev.push(prev[prev.length-1]+prev[prev.length-2]);
                break;
            default:
                prev.push(parseInt(cur));
                break;
        }
        return prev;
    },[]).reduce((acc,cur)=>acc+cur,0);
};