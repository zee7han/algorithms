function encode(arr){
    let res = ""
    arr.forEach(element => {
        res += element.length + "#" + element
    });
    return res
}

console.log(encode(["neet","code"]))


function decode(str){
    let res = []
    let i = 0

    while(i<str.length){
        j = i
        while(str[j] != "#"){
            j++
        }
        let wordLength = parseInt(str.slice(i,j))
        res.push(str.slice(j+1,j+1+wordLength))
        i = j+1+wordLength
    }
    return res
}

console.log(decode(encode(["neet","code"])))