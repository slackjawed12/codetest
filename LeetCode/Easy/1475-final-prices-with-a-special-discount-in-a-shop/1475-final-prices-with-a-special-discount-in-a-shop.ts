function finalPrices(prices: number[]): number[] {
    return prices.map((val, i)=>{
        const discount = prices.slice(i+1).find(v=>v<=val);
        
        if(discount === -1 || !discount) {
            return val
        }
        
        return val-discount;
    });
};