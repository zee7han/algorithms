function sort012(a,n) {
    let lo =0
    let mid = 0
    let hi = n-1
    while (mid <= hi) {
        if(a[mid] ===0){
            let tmp = a[mid]
            a[mid] = a[lo]
            a[lo] = tmp
            lo += 1
            mid += 1
        } else if(a[mid] === 1) {
            mid++
        } else {
            let tmp = a[mid]
            a[mid] = a[hi]
            a[hi] = tmp
            hi--
        }
    }
    return a
}
console.log(sort012( [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1], 12))