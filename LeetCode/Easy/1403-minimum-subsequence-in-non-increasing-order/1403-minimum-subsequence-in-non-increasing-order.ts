function minSubsequence(nums: number[]): number[] {
    nums.sort((x,y)=>y-x);
    
    let result = [];
    for(let i=1; i<=nums.length; i++){
        const temp = nums.slice(0, i);
        const rem = nums.slice(i);
        const sumOne = temp.reduce((acc,cur)=>acc+=cur, 0);
        const sumTwo = rem.reduce((acc,cur)=>acc+=cur, 0);
        
        if(sumOne>sumTwo) {
            result=temp;
            break;
        }
    }
    return result;
};