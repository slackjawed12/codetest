function maximum69Number (num: number): number {
    const numArr = num.toString().split("");
    const minIndex = numArr.findIndex(v=>v==='6');
    if(minIndex===-1){
        return num;
    }
    numArr.splice(minIndex, 1, '9');
    return parseInt(numArr.join(""));
};