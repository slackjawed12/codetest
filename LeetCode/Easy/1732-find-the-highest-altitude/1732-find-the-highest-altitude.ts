function largestAltitude(gain: number[]): number {
    const acc = gain.reduce((prev,cur,index)=>{
        prev.push(cur+prev[index]);
        return prev;
    },[0]);
    
    return Math.max(...acc)
};