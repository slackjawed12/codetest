function maxNumberOfBalloons(text: string): number {
    const store = text.split("").reduce((prev,cur)=>{
        prev.set(cur, prev.get(cur)?prev.get(cur)+1:1);
        return prev;
    }, new Map());
    const [b,a,l,o,n] = [store.get("b") ?? 0, store.get("a") ?? 0, store.get("l") ?? 0, store.get("o") ?? 0, 
                         store.get("n")??0];
    return Math.min(b,a,Math.floor(l/2),Math.floor(o/2),n);
};