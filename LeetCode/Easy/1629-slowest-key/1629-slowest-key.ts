function slowestKey(releaseTimes: number[], keysPressed: string): string {
    const result = keysPressed.split("").reduce((prev,cur,index)=>{
        if(index === 0) {
            return {
                ch: cur,
                duration: releaseTimes[0]
            }
        }
        
        const diff = releaseTimes[index] - releaseTimes[index-1]
        if(prev.duration < diff || (prev.duration === diff && prev.ch.charCodeAt(0) < cur.charCodeAt(0))) {
            return {
                ch: cur,
                duration: diff
            }
        }
        
        return prev;
    }, {ch:"", duration:0});
    
    return result.ch;
};