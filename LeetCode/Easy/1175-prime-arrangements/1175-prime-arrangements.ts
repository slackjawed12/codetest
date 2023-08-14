function numPrimeArrangements(n: number): number {
    const countPrime = (num: number)=>{
        const isPrime = Array.from(Array(num+1), (_, i)=>true);
        isPrime[0]=false;
        isPrime[1]=false;
        for(let i=2; i*i<=num; i++){
            if(isPrime[i]){
                for(let j=i*i; j<=num; j+=i){
                    isPrime[j]=false;
                }    
            }
        }
        return isPrime.filter(x=>x).length;
    }
    const mod = 10**9+7;
    const factorial = (num: number, start: number) => {
        let result = start;
        for (let i = 2; i <= num; i++) {
            result *= i;
            result %= mod;
        }
        return result;
    }
    
    const p = countPrime(n);
    const primeFactorial = factorial(p, 1);
    const answer = factorial(n-p, primeFactorial);
    
    return answer;
};