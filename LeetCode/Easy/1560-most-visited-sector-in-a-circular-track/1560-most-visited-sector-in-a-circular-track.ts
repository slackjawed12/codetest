function mostVisited(n: number, rounds: number[]): number[] {
    const info = rounds.slice(0, rounds.length-1).map((v,i)=>{
      return {
        start: v,
        end: rounds[i+1]
    };
    });
    
    const visit = Array.from(Array(n+1), (_)=>0);
    
    visit[info[0].start]++;
    
    info.forEach((val)=>{
        let current = val.start;
        while(current !== val.end) {
            const next = current % n + 1;
            visit[next]++;
            current = next;
        }
    })
    
    const maxVisited = visit.reduce((acc,cur)=>Math.max(acc,cur), 0);
    const result = visit.reduce((prev,cur, index)=>{
        if(cur===maxVisited)
            prev.push(index);
        
        return prev;
    }, []);
    
    return result;
};