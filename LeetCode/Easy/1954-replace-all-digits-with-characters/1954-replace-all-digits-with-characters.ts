function replaceDigits(s: string): string {
    const shift = (s:string, n:string)=>{
        return String.fromCharCode(s.charCodeAt(0) +parseInt(n))
    }

    return s.split("").map((v,i)=>{
        if(v.charCodeAt(0) >= "0".charCodeAt(0) && v.charCodeAt(0)<='9'.charCodeAt(0)) {
            return shift(s[i-1], v)
        }
        return v;
    }).join("");
};