
/* 
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
*/ 

function substr(s) {
    let max = 0
    let cur = 0
    let store_indexes = {}
    
    let i = 0
    while(i<s.length){
        if(!store_indexes.hasOwnProperty(s[i])){
            cur++
        } else {
            cur = Math.min(i-store_indexes[s[i]],cur+1)
        }
        max = Math.max(max,cur)
        store_indexes[s[i]] = i
        i++
    }
    return max
};

console.log(substr("dvdf"))
console.log(substr("abcabcaaadef"))
console.log(substr("bbbbb"))