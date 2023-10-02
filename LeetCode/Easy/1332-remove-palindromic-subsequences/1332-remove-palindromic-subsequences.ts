function removePalindromeSub(s: string): number {
    const isPalindrome = (s:string):boolean=>{
        let i = 0;
        let j = s.length -1;
        for(i=0; i<=j; i++) {
            if(s[i]===s[j]) {
                j--;
            } else {
                return false;
            }
        }
        
        return true;
    }
    
    if(isPalindrome(s)) {
        return 1;
    }
    
    return 2;
};