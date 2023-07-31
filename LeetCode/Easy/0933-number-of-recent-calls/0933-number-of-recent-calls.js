
var RecentCounter = function() {
    this.store = [];
};

/** 
 * @param {number} t
 * @return {number}
 */
RecentCounter.prototype.ping = function(t) {
    this.store.push(t);
    return this.store.filter(val=>val>=t-3000 && val<=t).length;
};

/** 
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = new RecentCounter()
 * var param_1 = obj.ping(t)
 */