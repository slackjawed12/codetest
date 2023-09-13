function countNegatives(grid: number[][]): number {
    return grid.reduce((prev, cur)=>{
       prev += cur.filter(x=>x<0).length;
        return prev;
    },0)
};