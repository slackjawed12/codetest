function checkIfExist(arr: number[]): boolean {
    let result = false;
    for(let i=0; i<arr.length; i++) {
        const sliced = [...arr.slice(0, i), ...arr.slice(i+1)];
        result ||= sliced.includes(2*arr[i]);
    }
    
    return result;
};