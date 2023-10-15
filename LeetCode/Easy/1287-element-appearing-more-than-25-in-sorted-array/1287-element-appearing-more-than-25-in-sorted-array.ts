function findSpecialInteger(arr: number[]): number {
    return arr.reduce((prev, cur, index)=>{
        const count = index === 0 ? 1 : cur === arr[index-1] ? prev.count+1 : 1;
        const element = count*4 >= arr.length ? cur : prev.element;
        return {count, element};
    }, {count:0, element: null}).element;
};