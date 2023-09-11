function countLargestGroup(n: number): number {
    const digits = new Map();
    for(let i=1; i<=n; i++) {
        let sums =0;
        let temp = i;
        while(temp > 0) {
            sums += temp%10;
            temp = Math.floor(temp/10);
        }
        digits.set(sums, digits.get(sums) ? digits.get(sums)+1 : 1);
    }
    const result = Array.from(digits).sort((x,y)=>y[1]-x[1]);
    
    return result.filter(item=>result[0][1]===item[1]).length;
};