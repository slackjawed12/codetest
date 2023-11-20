function decrypt(code: number[], k: number): number[] {
    return code.map((num,index)=>{
        if(k===0) {
            return 0;
        } else if(k>0) {
            const arr = Array.from(Array(k), (_, i)=>code[(index+i+1)%code.length]);
            return arr.reduce((acc,cur)=>acc+=cur, 0);
        } else {
            const arr = Array.from(Array(Math.abs(k)), (_,i)=>{
                const idx = index-i-1 < 0 ? code.length+(index-i-1): index-i-1;
                return code[idx]
            });
            return arr.reduce((acc,cur)=>acc+=cur,0);
        }
    });
};