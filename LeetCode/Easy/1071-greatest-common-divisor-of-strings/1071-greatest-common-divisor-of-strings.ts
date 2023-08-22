function gcdOfStrings(str1: string, str2: string): string {
    const [long, short] = str1>str2?[str1,str2]:[str2,str1];
    if(short==="") {
        return long;
    }
    
    const result = long.split(short);
    if(!result.reduce((prev,cur)=>{
        return prev && !!short.match(cur);
    }, true) || !result.includes('')){
        return ""
    };
    
    return gcdOfStrings(short, result.pop());
};