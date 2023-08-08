function oddCells(m: number, n: number, indices: number[][]): number {
    const rowInfo:number[] = Array.from(Array(m), (_)=>0);
    const colInfo:number[] = Array.from(Array(n), (_)=>0);
    indices.forEach(index=>{
        rowInfo[index[0]]++;
        colInfo[index[1]]++;
    }) 
    
    const odd = colInfo.filter(v=>v%2).length;
    const even = colInfo.filter(v=>!(v%2)).length;
    const result = rowInfo.reduce((acc, cur)=>{
       if(cur%2) {
          acc+=even;
       } else {
           acc+=odd;
       }
        return acc;
    },0)
    return result;
};