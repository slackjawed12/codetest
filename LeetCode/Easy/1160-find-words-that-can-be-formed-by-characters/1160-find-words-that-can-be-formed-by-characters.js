/**
 * @param {string[]} words
 * @param {string} chars
 * @return {number}
 */
var countCharacters = function(words, chars) {
    const count = (word)=> {
        return word.split("").reduce((prev, cur) => {
            prev.set(cur, prev.get(cur)?prev.get(cur)+1:1);
            return prev;
        }, new Map());
    };
    const isGood = function(word, store) {
        const wordCounter = count(word);
        for(const entry of wordCounter){
            const countOfStore = store.get(entry[0]) ?? 0;
            if(countOfStore < wordCounter.get(entry[0]))
                return false;
        }
        return true;
    }
    const store = count(chars);
    return words.reduce((acc,cur)=>{
       return acc += isGood(cur, store) ? cur.length : 0; 
    },0)
};