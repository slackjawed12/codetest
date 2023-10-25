function makeGood(s: string): string {
    const result = s.split("").reduce((prev,cur)=>{
        if(prev.length !== 0 && Math.abs(cur.charCodeAt(0) - prev[prev.length-1].charCodeAt(0)) === 32) {
            prev.pop();
            return prev;
        }
        
        prev.push(cur);
        return prev;
    },[])
    return result.join("");
};