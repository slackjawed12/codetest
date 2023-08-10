function heightChecker(heights: number[]): number {
    const expected = heights.slice().sort((x,y)=>x-y);
    return heights.reduce((acc,cur,i)=>acc += +(cur!==expected[i]),0)
};