/**
 * @param {string} s
 * @return {boolean}
 */
var checkRecord = function(s) {
    let absent=0;
    let lateConti = 0;
    for(let i=0; i<s.length; i++){
        if(s[i]==='A'){
            absent++;
            lateConti = 0;
        } else if(s[i]==='L'){
            lateConti++;
        } else{
            lateConti = 0;
        }
        
        if(lateConti === 3 || absent === 2){
            return false;
        }
    }
    
    return true;
};