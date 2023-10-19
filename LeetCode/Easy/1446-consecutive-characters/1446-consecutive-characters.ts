function maxPower(s: string): number {
    const arr = s.split("");
    let cur = arr[0];
    let conti = 1;
    let answer = conti;
    for(let i=1; i<arr.length; i++){
        if(arr[i] === cur) {
            conti++;
        } else {
            cur = arr[i]
            conti = 1;
        }
        answer = Math.max(answer, conti);
    }
    
    return answer;
};