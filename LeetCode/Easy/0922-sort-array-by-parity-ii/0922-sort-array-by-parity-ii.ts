function sortArrayByParityII(nums: number[]): number[] {
    
    for(let i=0; i<nums.length; i++) {
        if(nums[i]%2 !== i%2) {
            const parity = i%2;
            for(let j=i+1; j<nums.length; j++) {
                if(nums[j]%2===parity) {
                    const temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                    break;
                }
            }
        }
    }
    
    return nums;
};