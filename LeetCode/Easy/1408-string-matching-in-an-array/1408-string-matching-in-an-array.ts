function stringMatching(words: string[]): string[] {
    return words.filter((word, i)=>{
        const include = words.filter((v,j)=>i!=j).filter(val=>val.includes(word));
        return include.length > 0;
    })
};