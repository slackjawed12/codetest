function arrayRankTransform(arr: number[]): number[] {
    const copy = arr.map((val, i)=>({
        val,
        index:i,
        rank:1
    }));
    copy.sort((o1,o2)=>o1.val-o2.val);

    const ordered = copy.reduce((prev, cur, i)=>{
        if (i===0) {
            prev.push(cur);
            return prev;
        }

        const prevRank = prev[prev.length-1].rank
        prev.push({
            ...cur,
            rank: prev[i-1].val === cur.val ? prevRank : prevRank +1
        });
        return prev;
    },[])

    ordered.sort((o1,o2)=>o1.index-o2.index);
    return ordered.map((v)=>v.rank);
};