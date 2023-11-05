function maxScore(s: string): number {
    const array = Array.from(Array(s.length-1), (_,i)=>i+1);
    const splitString = s.split("");
    const substrings = array.map(v=>([splitString.slice(0,v), splitString.slice(v)]))
    const scores = substrings.map(v=>v[0].filter(x=>x==='0').length + v[1].filter(x=>x==='1').length);
    return Math.max(...scores)
};