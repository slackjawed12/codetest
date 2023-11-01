function minOperations(logs: string[]): number {
    const depth = logs.reduce((prev,cur)=>{
        if(cur === './') {
            return prev;
        }
        if(cur === '../') {
            return prev === 0? prev : prev-1;
        }
        return prev+1;
    }, 0)
    
    return depth;
};