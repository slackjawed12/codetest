function frequencySort(nums: number[]): number[] {
    const store = nums.reduce((prev,cur)=>{
        const item = prev.get(cur);
       if(item) {
           prev.set(cur, item+1);
       }
       prev.set(cur, item?item+1:1);

        return prev;
    }, new Map());

    nums.sort((x,y)=>store.get(x) === store.get(y) ? y - x : store.get(x)-store.get(y));
    
    return nums;
};