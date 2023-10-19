function threeConsecutiveOdds(arr: number[]): boolean {
    let conti = 0;
    for(let i=0; i<arr.length; i++){
        if (arr[i] % 2) {
            conti++;
        } else {
            conti =0;
        }
        
        if(conti===3) {
            return true;
        }
    }
    
    return false;
};