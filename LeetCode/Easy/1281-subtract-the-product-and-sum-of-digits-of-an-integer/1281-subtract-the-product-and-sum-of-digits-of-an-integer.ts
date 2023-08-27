function subtractProductAndSum(n: number): number {
    const numString = n.toString().split("");
    const product = numString.reduce((acc,cur)=>acc*=parseInt(cur), 1);
    const sum = numString.reduce((acc,cur)=>acc+=parseInt(cur),0);
    
    return product-sum;
};