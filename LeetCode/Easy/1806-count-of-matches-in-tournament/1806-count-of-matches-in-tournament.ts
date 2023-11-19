function numberOfMatches(n: number): number {
    let res = n;
    let matches = 0;
    while (res !==1) {
        matches += Math.floor(res/2);
        res = Math.floor(res/2) + res%2
    }

    return matches;
};