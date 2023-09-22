function sortByBits(arr: number[]): number[] {
    const bitcount = (num:number)=>{
        let count = 0;
        while(num!=0) {
            count += num&1;
            num = num >> 1;
        }
        return count;
    }
    
    const compare = (o1, o2)=>{
        const bitcount1 = bitcount(o1);
        const bitcount2 = bitcount(o2);
        return bitcount1 !== bitcount2 ? bitcount1 - bitcount2 : o1-o2;
    }
    
    
    return arr.sort(compare)
};