/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    if(n===0) {
        return true;
    } else if(flowerbed.length===1){
        return flowerbed[0]===0;
    }
    
    if(flowerbed[0] === 0 && flowerbed[1]===0){
        flowerbed[0] =1;
        n--;
    }
    
    for(let i = 1; i<flowerbed.length-1; i++){
        if(flowerbed[i] === 0 && flowerbed[i-1]===0 && flowerbed[i+1]===0){
            flowerbed[i] = 1;
            n--;
        }
        
        if(n===0){
            break;
        }
    }
    
    if(n===0){
        return true;
    } else if (flowerbed[flowerbed.length-2]===0 && flowerbed[flowerbed.length-1]===0) {
        return n-1===0;
    } else {
        return n===0;
    }
};