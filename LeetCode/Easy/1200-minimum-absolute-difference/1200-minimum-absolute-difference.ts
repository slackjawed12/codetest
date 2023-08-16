function minimumAbsDifference(arr: number[]): number[][] {
    const sorted = arr.slice().sort((x,y)=>x-y);
    let minDiff = Infinity;
    for(let i=0; i<sorted.length-1; i++){
        minDiff = Math.min(minDiff, Math.abs(sorted[i]-sorted[i+1]));
    }
    
    const answer =[];
    for(let i=0; i<sorted.length-1; i++){
        if(Math.abs(sorted[i]-sorted[i+1])===minDiff)
            answer.push([sorted[i], sorted[i+1]]);
    }
    
    return answer;
};