function specialArray(nums: number[]): number {
    const max = Math.max(...nums);
    let result = -1;
    for(let i=0; i<=max; i++){
        const count = nums.filter(v=>v>=i).length;
        if(count === i) {
            result = count;
            break;
        }
    }
    return result;
};