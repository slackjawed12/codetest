function reorderSpaces(text: string): string {
    const words = text.trim().split(" ").filter(v=>v.length>=1)
    const spaces = text.split("").reduce((prev,cur)=>prev += +(cur===' '), 0);
    const divider = words.length === 1 ? 1 : words.length -1;
    const result = words.reduce((prev,cur,index)=>{
        const space = index === words.length- 1 ? prev.rem : Math.floor(spaces/divider);
        return {
            acc: prev.acc + cur + " ".repeat(space),
            rem: prev.rem - space
        }
    }, {
        acc: "",
        rem: spaces
    });
    
    return result.acc
};