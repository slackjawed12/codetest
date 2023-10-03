function busyStudent(startTime: number[], endTime: number[], queryTime: number): number {
    const converted = startTime.map((v,i)=>{
        return {
            start: v,
            end: endTime[i]
        }
    });
    
    return converted.filter(v=>queryTime>=v.start && queryTime <= v.end).length;
};