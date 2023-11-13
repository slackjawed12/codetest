function nearestValidPoint(x: number, y: number, points: number[][]): number {
    let answer = -1;
    let value = Infinity;
    for(let i=0;i<points.length; i++){
        const isValid = (x === points[i][0]) || (y===points[i][1])
        if (isValid) {
            const dist = Math.abs(x-points[i][0]) + Math.abs(y-points[i][1])
            if(value > dist) {
                answer = i;
                value = dist
            }
        }
    }

    return answer;
};