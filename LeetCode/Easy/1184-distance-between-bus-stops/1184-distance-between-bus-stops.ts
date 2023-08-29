function distanceBetweenBusStops(distance: number[], start: number, destination: number): number {
    const len = distance.length;
    
    let clock = start;
    let distOne = 0;
    while(clock!==destination) {
        distOne += distance[clock];
        clock = (clock+1)%len;
    }
    
    let counterClock = start;
    let distTwo = 0;
    while(counterClock !== destination) {
        counterClock = counterClock === 0 ? len-1 : (counterClock - 1)%len;
        distTwo += distance[counterClock];
    }
    
    return Math.min(distOne, distTwo);
};