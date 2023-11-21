function sortSentence(s: string): string {
    const parseInfo = s.split(" ").map((w)=>{
        const word = w.slice(0, w.length-1);
        const order = parseInt(w.slice(-1));
        return {
            word,
            order
        }
    })
    parseInfo.sort((o1,o2)=>o1.order-o2.order);
    const result = parseInfo.reduce((prev,cur)=>{
        return prev + cur.word + " ";
    },"")
    return result.slice(0,result.length-1);
};