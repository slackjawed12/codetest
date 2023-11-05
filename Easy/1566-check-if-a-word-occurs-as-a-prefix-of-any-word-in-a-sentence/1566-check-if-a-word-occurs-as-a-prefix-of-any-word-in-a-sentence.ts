function isPrefixOfWord(sentence: string, searchWord: string): number {
    const result = sentence.split(" ").findIndex(w=>w.startsWith(searchWord));
    return result === -1 ? -1 : result +1
};