function xorOperation(n: number, start: number): number {
    return Array.from(Array(n), (_, i)=>start+2*i).reduce((prev,cur,i)=>{
        if(i===0) {
            return cur
        }
        return prev ^= cur
    }, 0);
};