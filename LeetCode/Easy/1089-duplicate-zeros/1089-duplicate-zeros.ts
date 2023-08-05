/**
 Do not return anything, modify arr in-place instead.
 */
function duplicateZeros(arr: number[]): void {
    let isDuplicated = false;
    for(let i=0; i<arr.length; i++){
        if(arr[i]===0 && !isDuplicated) {
            arr.splice(i+1, 0, 0);
            arr.pop();
            isDuplicated = true;
        } else {
            isDuplicated=false;
        }
    }
};