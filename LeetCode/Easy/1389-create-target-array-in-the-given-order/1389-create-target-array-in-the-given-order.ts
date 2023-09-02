function createTargetArray(nums: number[], index: number[]): number[] {
    const convertToTuple = (arr1, arr2) => {
        return arr1.map((val, i)=>{
            return [val, arr2[i]];
        })
    };
    
    const tuple = convertToTuple(nums, index);
    
    return tuple.reduce((prev,cur)=>{
       prev.splice(cur[1], 0, cur[0]);
        return prev;
    },[]);
};