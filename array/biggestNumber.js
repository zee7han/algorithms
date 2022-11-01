function biggestNumber(arr) {
    arr = arr.sort((first, second) => {
        var firstsecond = '' + first + second;
        var secondfirst = '' + second + first;
        return firstsecond > secondfirst ? -1 : 1;
    })
    return arr.join("")
}

let arr = [54, 546, 548, 60]
console.log(biggestNumber(arr));