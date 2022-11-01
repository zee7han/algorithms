function rev_sentences(s) {
    let words = []
    let i=0;

    while(i<s.length) {
        if(s[i] !== " "){
            let st = i
            while(i< s.length && s[i] !== " ") {
                i++
            }
            words.push(s.slice(st,i))
        }
    i++
    }
    return words.reverse().join(" ")
}

console.log(rev_sentences("you are here"))
console.log(rev_sentences("    I am here"))
console.log(rev_sentences("No I am not there    "))