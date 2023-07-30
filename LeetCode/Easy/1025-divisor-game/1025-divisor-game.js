/**
 * @param {number} n
 * @return {boolean}
 */
var divisorGame = function(n) {
    const getDivisors = (num)=>{
        const result = [];
        for(let i=1; i*i<=num; i++){
            if(!(num%i)) {
                if(i !== 1) result.push(num/i);
                
                if(num/i !== i) result.push(i);
            }
        }
        return result;
    }
    
    const dp = Array.from(Array(n+1), (_,i)=>false);
    
    for(let i=2; i<=n; i++){
        const divisors = getDivisors(i);
        
        for(let j=0; j<divisors.length; j++){
            if(!dp[i-divisors[j]]) {
                dp[i]=!dp[i-divisors[j]];
                break;
            }
        }
    }
    return dp[n];
};