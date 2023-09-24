function kidsWithCandies(candies: number[], extraCandies: number): boolean[] {
    const greatest = candies.reduce((prev,cur)=>Math.max(prev, cur),0);
    
    return candies.map((v)=>(v+extraCandies)>=greatest);
};