function modifyString(s: string): string {
    const alphabet = "abcdefghijklmnopqrstuvwxyz".split("");
    const result = s.split("").reduce((prev,cur,index)=>{
       if(cur !== '?') {
           return [...prev, cur];
       }
       
        if(index === 0) {
            const added = alphabet.find(v=>v!==s[index+1]);
            return [...prev, added];
        }
        
        if(index === s.length-1) {
            const added = alphabet.find(v=>v!==prev[index-1]);
            return [...prev, added];
        }
        
        const added = alphabet.find(v=>v!==prev[index-1] && v !== s[index+1]);
        return [...prev, added];
        
    },[])
    
    return result.join("");
};