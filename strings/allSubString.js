function allSubString(str) {
    for(let i=0; i<str.length; i++){
        let temp=""
        for(let j=i; j<str.length; j++){
            temp += str[j]
            console.log(temp);
        }
    }
}

allSubString("geekya")