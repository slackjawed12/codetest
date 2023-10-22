function numEquivDominoPairs(dominoes: number[][]): number {
    const store = dominoes.reduce((prev, cur, index) =>{
        const nrKey = cur[0]*10+cur[1];
        const rotKey = cur[1]*10+cur[0];
        const nrVal = prev.get(nrKey);
        const rotVal = prev.get(rotKey);
        if(!nrVal && !rotVal) {
            prev.set(nrKey, 1);
        } else if (nrVal) {
            prev.set(nrKey, prev.get(nrKey)+1)
        } else {
            prev.set(rotKey, prev.get(rotKey)+1)
        }
        return prev;
    }, new Map());
    
    return Array.from(store).reduce((prev,cur)=>{
       return prev += Math.floor(cur[1] * (cur[1]-1) /2);
    },0)
};