function minRotatedArray(arr) {
    let res = arr[0]
    let l = 0
    let r = arr.length -1

    while(l<r){
        if(arr[l] < arr[r]){
            res = Math.min(res, arr[l])
            break;
        } else {
            let mid = Math.floor((r+l)/2)
            res = Math.min(arr[mid],res)
            if(arr[l] <= arr[mid]){
                l = mid+1
            } else {
                r = mid-1
            }
        }
    }
    return res
}

console.log(minRotatedArray([3,4,5,1,2]))