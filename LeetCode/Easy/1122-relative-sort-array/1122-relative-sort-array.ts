function relativeSortArray(arr1: number[], arr2: number[]): number[] {
    const store = new Map(Array.from(arr2, (v,i)=>[v, i]));
    
    return arr1.sort((o1,o2)=>{
        const i1 = store.get(o1) ?? -1;
        const i2 = store.get(o2) ?? -1;
        
        if(i1>=0) {
            return i2>=0 ? i1-i2 : -1
        }
        
        return i2>=0 ? 1 : o1-o2;
    });
};