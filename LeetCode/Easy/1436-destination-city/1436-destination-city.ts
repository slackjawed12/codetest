function destCity(paths: string[][]): string {
    const store = new Map();
    paths.forEach(v=>store.set(v[0], v[1]))

    let cur = paths[0][0];
    let prev;
    while(cur) {
        prev = cur
        cur = store.get(cur)
    }
    
    return prev;
};