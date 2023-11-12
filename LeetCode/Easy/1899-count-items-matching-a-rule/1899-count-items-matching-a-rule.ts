function countMatches(items: string[][], ruleKey: string, ruleValue: string): number {
    const result = items.filter((item)=>{
        const index = ruleKey === 'type' ? 0 : ruleKey === 'color' ? 1 : 2;
        return item[index] === ruleValue
    })

    return result.length;
};