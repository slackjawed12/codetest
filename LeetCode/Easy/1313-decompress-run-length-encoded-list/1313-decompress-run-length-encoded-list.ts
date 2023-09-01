function decompressRLElist(nums: number[]): number[] {
    const temp = nums.reduce((prev,cur,i)=>{
        if(!(i%2)) {
            prev.push({
                freq:cur,
                val:nums[i+1]
            })
            
            return prev;
        }
        
        return prev;
    },[]);
    
    return temp.reduce((prev, cur)=>{
       return prev=[...prev, ...Array.from(Array(cur.freq), (_)=>cur.val)] 
    },[])
};