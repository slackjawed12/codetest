function decode(encoded: number[], first: number): number[] {
    const result = encoded.reduce((prev,cur,index)=>{
        const a = prev[prev.length-1];
        const ans = a^cur;
        prev.push(ans);
        return prev;
    },[first]);

    return result;
};