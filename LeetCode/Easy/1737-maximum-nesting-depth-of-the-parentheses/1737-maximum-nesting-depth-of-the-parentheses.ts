function maxDepth(s: string): number {
    const operation = s.split("").reduce((prev,cur)=>{
        if(cur === "(") {
            prev.stack.push(cur)
        } else if(cur === ")") {
            prev.max = Math.max(prev.max, prev.stack.length)
            prev.stack.pop()
        }

        return prev;
    }, {stack:[], max: 0})

    return operation.max;
};