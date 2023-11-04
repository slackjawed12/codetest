function countGoodRectangles(rectangles: number[][]): number {
    const maxSquareLengths = rectangles.map((v)=>Math.min(...v));
    const maxLength = Math.max(...maxSquareLengths);
    const count = maxSquareLengths.filter(v=>v===maxLength).length;
    return count;
};