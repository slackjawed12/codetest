function countOdds(low: number, high: number): number {
    const lowOdd = low %2 ? low : low+1;
    const highOdd = high%2 ? high:high-1;
    return Math.floor((highOdd-lowOdd)/2)+1;
};