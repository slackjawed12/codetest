function sumZero(n: number): number[] {
    if(n%2) {
        return Array.from(Array(n), (_,i)=>{
            return -Math.floor(n/2)+i;
        })
    }
    else {
        const half = Array.from(Array(n/2), (_, i)=>{
            return -(n/2)+i;
        })
        return [...half,...half.map(v=>Math.abs(v))];
    }
};