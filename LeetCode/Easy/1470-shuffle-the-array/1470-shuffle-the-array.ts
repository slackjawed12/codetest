function shuffle(nums: number[], n: number): number[] {
    return nums.slice(0, nums.length/2).reduce((prev, cur, index)=>{
        return [...prev, cur, nums[index+nums.length/2]]
    }, [])
};