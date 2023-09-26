function sumOddLengthSubarrays(arr: number[]): number {
    let result = 0;
    for(let i=1; i<=arr.length; i+=2){
        for(let start = 0; start <= arr.length - i; start++) {
            result += arr.slice(start, start+i).reduce((acc,cur)=>acc+=cur, 0);
        }
    }
    
    return result;
};