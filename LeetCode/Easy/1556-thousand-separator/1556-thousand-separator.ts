function thousandSeparator(n: number): string {
    const numArray = String(n).split("");
    let count = 1;
    for(let i=numArray.length-1; i>0; i--){
        if(count%3===0) {
            numArray.splice(i, 0,'.')
        }
        count++;
    }
    return numArray.join("");
}