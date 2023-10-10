function numWaterBottles(numBottles: number, numExchange: number): number {
    let result = 0;
    let filled = numBottles;
    let empty = 0;
    while (filled != 0) {
        result += filled;
        empty += filled;
        filled = 0;
        filled += Math.floor(empty/numExchange);
        empty -= Math.floor(empty/numExchange)*numExchange;
    }
    
    return result;
};