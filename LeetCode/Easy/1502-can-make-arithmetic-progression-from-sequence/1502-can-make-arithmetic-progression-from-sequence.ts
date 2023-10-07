function canMakeArithmeticProgression(arr: number[]): boolean {
    arr.sort((x,y)=>x-y);
    let isProgression = true;
    const initialDiff = arr[0]-arr[1];
    for(let i=0; i<arr.length-1; i++){
        if (arr[i]-arr[i+1] !== initialDiff) {
            isProgression = false;
            break;
        }
    }
    
    return isProgression;
};