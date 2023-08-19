function findOcurrences(text: string, first: string, second: string): string[] {
    const words = text.split(" ")
    const info = words.map((word,i)=>{
        if(i==0 || i==1)
            return {word,}
        
        return {
            word: word,
            first: words[i-2],
            second: words[i-1]
        }
    });
    
    const result = info.filter(i=> i.first===first && i.second===second).map(r=>r.word);
    
    return result
};