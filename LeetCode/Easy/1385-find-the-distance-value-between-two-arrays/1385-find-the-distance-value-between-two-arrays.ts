function findTheDistanceValue(arr1: number[], arr2: number[], d: number): number {
    const answer = arr1.reduce((prev,cur)=>{
        const isInclude = arr2.find(v=>Math.abs(cur-v)<=d);
        
        return prev += isInclude == undefined ? 1 : 0;
    }, 0);
    
    return answer;
};