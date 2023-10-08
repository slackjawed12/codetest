function canBeEqual(target: number[], arr: number[]): boolean {
    const getCounter = (nums:number[])=>{
        return nums.reduce((prev,cur)=>{
            prev.set(cur, prev.get(cur) ? prev.get(cur)+1:1);
            return prev;
        }, new Map());
    };
    
    const targetCounter = getCounter(target);
    const arrCounter = getCounter(arr);
    
    return Array.from(targetCounter).reduce((prev, [k,v]) => prev &&= arrCounter.get(k) === v, true);
};