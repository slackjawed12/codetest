function checkIfPangram(sentence: string): boolean {
    const store = new Set(sentence.split(""));
    return Array.from(store).length === 26;
};