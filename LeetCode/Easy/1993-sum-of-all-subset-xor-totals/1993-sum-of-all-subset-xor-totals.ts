function subsetXORSum(nums: number[]): number {
    const s = 2 ** nums.length;
    let ans = 0;
    for(let i=0; i<s; i++){
        const mask = i;
        const arr = Array.from(Array(nums.length), (_,i)=>i)
                    .filter((v,idx)=>((mask >>> idx) & ((2**v)>>>idx)) === 1).map(v=>nums[v]);
        ans += arr.reduce((acc,cur)=>acc^=cur,0);
    }

    return ans;
};