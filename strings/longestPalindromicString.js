function longestPalindrome(str){
    let longest = ""
    for(let i=0; i<str.length; i++){
        let cur1 = getPalindromeString(str,i,i)
        let cur2 = getPalindromeString(str,i,i+1)
        let longerPalindrome = cur1.length > cur2.length ? cur1 : cur2
        if(longerPalindrome.length > longest.length){
            longest = longerPalindrome
        }
    }
    return longest
}

function getPalindromeString(str,i,j){
    while(i >= 0 && j < str.length && str[i] == str[j]){
        i--
        j++
    }
    return str.slice(i+1,j)
}


console.log(longestPalindrome("babad"))