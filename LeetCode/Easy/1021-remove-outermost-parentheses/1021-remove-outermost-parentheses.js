/**
 * @param {string} s
 * @return {string}
 */
var removeOuterParentheses = function(s) {
    const temp = [];
    return s.split("").reduce((prev,cur)=>{
        if(prev.count===0){
            return {
                result:prev.result,
                count:1
            };
        }        
        
        if(prev.count===1) {
            if(cur===')'){
                const added = temp.join("");
                temp.splice(0,temp.length);
                return {
                    result:prev.result+added,
                    count:0
                }
            }
        }
        
        temp.push(cur);
        return {
            result:prev.result,
            count:cur==='(' ? prev.count+1 : prev.count-1
        }
    },{
        result:"",
        count:0
    }).result;
};