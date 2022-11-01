function longestSubstring(str){
    let max = 0;
    let start = 0;
    let map = {};
    for (let i = 0; i < str.length; i++) {
        if (map[str[i]] > start) {
            start = map[str[i]]
        }
        map[str[i]] = i
        max = Math.max(max, i - start + 1)
    }
    return max
};

console.log(longestSubstring("abcabcbc"))