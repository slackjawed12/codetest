function sumOfUnique(nums: number[]): number {
    const store = nums.reduce((prev,cur)=>{
        prev.set(cur, prev.get(cur) ? prev.get(cur)+1: 1);
        return prev;
    }, new Map())
    console.log(Array.from(store));
    return Array.from(store).filter(v=>v[1]===1).map(v=>v[0]).reduce((acc,cur)=>acc+=cur, 0);
};