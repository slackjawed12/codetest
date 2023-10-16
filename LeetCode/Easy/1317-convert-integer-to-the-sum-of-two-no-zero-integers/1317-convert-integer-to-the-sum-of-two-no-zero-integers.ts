function getNoZeroIntegers(n: number): number[] {
    const isNonZero = (num: number) =>{
        let temp = num;
        while(temp>0) {
            if (temp%10 === 0) {
                return false;
            }
            
            temp = Math.floor(temp/10);
        }
            
        return true;
    }
    
    let answer = [];
    for(let i=1; i<= Math.floor(n/2); i++){
        const a = i;
        const b = n - i;
        if(isNonZero(a) && isNonZero(b)) {
            answer = [a, b];
            break;
        }
    }
    
    return answer;
};