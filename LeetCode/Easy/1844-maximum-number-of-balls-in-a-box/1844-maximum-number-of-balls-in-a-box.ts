function countBalls(lowLimit: number, highLimit: number): number {
    const store = Array.from(Array(highLimit-lowLimit + 1), (_, i)=>i+lowLimit).reduce((prev,cur)=>{
        const digit = cur.toString().split('').map(v=>parseInt(v)).reduce((acc,cur)=>acc+=cur, 0);
        const count = prev.get(digit);
        if(count) {
            prev.set(digit, count+1);
            return prev;
        }
        prev.set(digit, 1);
        return prev;
    },new Map());

    return [...store.values()].reduce((prev,cur)=>Math.max(prev,cur),0);
};