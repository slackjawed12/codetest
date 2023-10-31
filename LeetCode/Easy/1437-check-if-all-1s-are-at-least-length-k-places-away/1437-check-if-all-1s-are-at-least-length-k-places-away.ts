function kLengthApart(nums: number[], k: number): boolean {
    let conti = 0;
    let leadingZero = true;
    for(let i=0; i<nums.length; i++) {
        if(leadingZero) {
            if(nums[i]===1) {
                leadingZero = false;
            }
            continue;
        }
        
        if(nums[i]===1) {
            if(conti < k) {
                return false;
            }
            conti = 0;
        } else {
            conti++;
        }
    }
    
    return true;
};