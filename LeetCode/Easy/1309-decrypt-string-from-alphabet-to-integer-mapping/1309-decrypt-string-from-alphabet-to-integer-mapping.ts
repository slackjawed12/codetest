function freqAlphabets(s: string): string {
    const result = [];
    const arr = s.split("");
    const temp = []
    for(let i=0; i<arr.length; i++){
        let isEscape = false;
        for(let j = i + 1; j < Math.min(arr.length, i + 3); j++){
            if(arr[j]==='#') {
                isEscape = true;
                break;
            }    
        }
                
        if(isEscape) {
            temp.push(arr[i])
        } else if(arr[i]==='#') {
            const num = parseInt(temp.join(""));
            result.push(String.fromCharCode(num+96));
            temp.splice(0, temp.length);
            isEscape=false;
        } else {
            const num = parseInt(arr[i]);
            result.push(String.fromCharCode(num+96));
        }
    }
    
    return result.join("");
};