function generateTheString(n: number): string {
    return n%2? "a".repeat(n) : "a".repeat(n-1) +"b";
};