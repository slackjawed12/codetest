function numberOfSteps(num: number): number {
    return numberOfStepsHelper(num, 0);
};

function numberOfStepsHelper(num: number, result: number): number{
    if(num===0)
        return result;
    
    return numberOfStepsHelper(num%2 ? num-1 : num/2, result+1);
}