function distributeCandies(candies: number, num_people: number): number[] {
    let n = num_people;
    let result = Array.from(Array(n), (_)=>0);
    
    let temp = 1;
    let i = 0;
    while(candies!==0) {
        const dist = Math.min(candies, temp);
        result[i] += dist;
        candies -= dist;
        temp++;
        i = (i+1) % n;
    }
    
    return result;
};