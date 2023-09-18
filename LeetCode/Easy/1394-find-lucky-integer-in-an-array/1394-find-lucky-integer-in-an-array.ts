function findLucky(arr: number[]): number {
    const frequency = arr.reduce((prev,cur)=>{
        prev.set(cur, prev.get(cur) ? prev.get(cur) + 1 : 1);
        return prev;
    }, new Map());
    
    
    const result = Array.from(frequency)
        .filter((v)=>v[0]===v[1])
        .reduce((acc,cur)=>Math.max(acc, cur[0]), -1);
    
    return result;
};