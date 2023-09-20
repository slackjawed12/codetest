function restoreString(s: string, indices: number[]): string {
   const temp = s.split("").reduce((prev,cur, i)=>{
       prev.set(indices[i], cur)
       return prev;
   }, new Map());
   
   const result = Array.from(temp).sort((o1,o2)=>o1[0]-o2[0]).map(r=>r[1]).join("");
   
   return result;
};