function average(salary: number[]): number {
    const max = salary.reduce((prev,cur)=>Math.max(prev, cur), 0);
    const min = salary.reduce((prev,cur)=>Math.min(prev, cur), Infinity);
    const sum = salary.filter(v=>v!==max && v!==min).reduce((prev,cur)=>prev+=cur, 0);
    const avg = sum/(salary.length-2);
    return parseFloat(avg.toFixed(5));
};