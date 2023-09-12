function sortString(s: string): string {
    const splited = s.split("");
    let result = [];
    let isIncreasing = true;
    while(splited.length>0){
        const distinct = splited.filter((it, i, _self)=>_self.indexOf(it)===i)
        distinct.sort((x,y)=>(x.charCodeAt(0)-y.charCodeAt(0))*(isIncreasing?1:-1));
        result = [...result, ...distinct];
        for(const c of distinct) {
            splited.splice(splited.indexOf(c), 1);
        }
        isIncreasing = !isIncreasing;
    }
    return result.join("");
};