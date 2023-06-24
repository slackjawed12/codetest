/**
 * // Definition for a Node.
 * function Node(val, children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {Node|null} root
 * @return {number[]}
 */
var preorder = function(root) {
    let answer = [];
    if(root!==null){
        preorderHelper(root, answer);
    }
    
    return answer;
};

var preorderHelper = function x (root, cur){
    if(root !== null) {
        cur.push(root.val);
        for(let i=0; i<root.children.length; i++){
            x(root.children[i], cur);
        }
    }
}