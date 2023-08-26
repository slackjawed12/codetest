function minTimeToVisitAllPoints(points: number[][]): number {
    const shortest = (p1:number[], p2:number[]) => {
        const dx = Math.abs(p2[0]-p1[0]);
        const dy = Math.abs(p2[1]-p1[1]);
        
        return Math.max(dx, dy)
    };
    
    return points.slice(1).reduce((prev,cur)=>{
        const added = shortest(cur, prev.start);
        return prev = {
            start:cur,
            second:prev.second+added
        }
    }, {start:points[0], second:0}).second;
};