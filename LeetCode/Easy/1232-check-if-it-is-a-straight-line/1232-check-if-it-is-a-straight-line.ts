function checkStraightLine(coordinates: number[][]): boolean {
    const [first, second] = coordinates.slice(0,2);
    const firstVector = [second[0]-first[0], second[1]-first[1]];
    const result = coordinates.slice(1).reduce((prev,[x,y])=>{
        const curVector = [x-first[0], y-first[1]];
        return prev && (curVector[0]*firstVector[1] - curVector[1]*firstVector[0] === 0)
    }, true)
    return result;
};