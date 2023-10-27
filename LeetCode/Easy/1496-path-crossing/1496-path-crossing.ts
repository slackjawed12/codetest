function isPathCrossing(path: string): boolean {
    const result = path.split("").reduce((prev,cur) => {
        let [x, y] = prev.pos;
        switch(cur) {
            case 'N':
                y += 1;
                break;
            case 'S':
                y -= 1;
                break;
            case 'E':
                x += 1;
                break;
            case 'W':
                x -= 1;
                break;
            default:
                break;
        };
        prev.isCrossed ||= prev.info.has(`${x},${y}`);
        prev.info.add(`${x},${y}`);
        prev.pos = [x,y];
        return prev;
    },{info:new Set([`0,0`]), pos:[0,0], isCrossed: false});
    
    return result.isCrossed;
};