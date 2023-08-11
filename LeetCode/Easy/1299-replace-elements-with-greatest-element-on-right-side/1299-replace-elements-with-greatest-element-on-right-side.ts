function replaceElements(arr: number[]): number[] {
    let maxIndex = 0;
    let maxNum = 0;
    const answer:number[]=[];
    for(let i=0; i<arr.length-1; i++){
        if(i===maxIndex){
            maxNum=0;
            for(let j=i+1; j<arr.length; j++){
                if(arr[j]>maxNum){
                    maxNum=arr[j];
                    maxIndex=j;
                }
            }
        }
        answer.push(maxNum);
    }
    
    answer.push(-1);
    return answer;
};