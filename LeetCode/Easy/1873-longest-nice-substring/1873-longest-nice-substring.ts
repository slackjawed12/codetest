function longestNiceSubstring(s: string): string {
    const isNiceString = (s:string):boolean =>{
        const stringList = s.split("")
        const store = new Set(stringList)
        return stringList.reduce((prev,cur)=>{
            const hasBoth = store.has(cur.toLowerCase()) && store.has(cur.toUpperCase())
            return prev && hasBoth
        }, true)
    }

    const getSubstrings = (s:string):string[] =>{
        const answer = []
        for(let i=0; i<s.length; i++) {
            for (let j=i+1; j<=s.length; j++) {
                answer.push(s.slice(i,j))
            }
        }
        return answer;
    }

    const substrings = getSubstrings(s);
    return substrings.reduce((prev,cur)=>{
        if(isNiceString(cur) && cur.length > prev.length) {
            return cur
        }

        return prev;
    }, "");
};