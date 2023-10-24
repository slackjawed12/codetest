function findKthPositive(arr: number[], k: number): number {
    const store = new Set(arr);
    let count = 0;
    let answer = 0;
    for(let i=1; i<=arr[arr.length-1]; i++) {
        if (!(store.has(i))) {
            count += 1;
        }
        
        if(count === k) {
            answer = i;
            break;
        }
    }
    
    if(answer === 0) {
        answer = arr[arr.length-1]+(k-count);
    }
    return answer;
};