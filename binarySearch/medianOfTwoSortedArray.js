function median(arr1, arr2) {
    let A = arr1
    let B = arr2
    let totalLength = A.length + B.length
    let half = Math.floor(totalLength / 2)

    if (A.length > B.length) {
        let temp = B
        B = A
        A = temp
    }

    let l = 0
    let r = A.length - 1
    while (true) {
        let midA = Math.floor((l + r) / 2)
        let midB = half - midA - 2

        let Aleft = A[midA]
        let ARight = A[midA + 1]
        let Bleft = B[midB]
        let BRight = B[midB + 1]

        if (Aleft <= BRight && Bleft <= ARight) {
            if (totalLength % 2 !== 0) {
                return Math.min(ARight, BRight)
            } else {
                return (Math.max(Aleft, Bleft) + Math.min(BRight, ARight)) / 2
            }

        } else if (Aleft > BRight) {
            r = midA - 1
        } else {
            l = midA + 1
        }
    }
}


console.log(median([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5]))