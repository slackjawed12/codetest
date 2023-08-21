function reverseOnlyLetters(s: string): string {
    const isAlphabet = (s:string)=>{
        const ascii = s.charCodeAt(0)
        return (ascii >= "a".charCodeAt(0) && ascii <= "z".charCodeAt(0)) || (ascii >= "A".charCodeAt(0) && ascii <= "Z".charCodeAt(0));
    }
    
    const stack = s.split("").filter(c=>isAlphabet(c));
    
    return s.split("").map(c=>{
        if(isAlphabet(c)) {
            return stack.pop();
        }
        
        return c;
    }).join("");
};