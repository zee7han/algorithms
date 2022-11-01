function binarySearch(arr, low, high, x) {
    if(high >= low) {
        let mid = Math.round(low + (high - low)/2)
        if(x == arr[mid]) {
            return (mid)
        } else if(x > arr[mid]){
            return binarySearch(arr,mid+1,high,x)
        } else {
            return binarySearch(arr,low,mid-1,x)
        }
    } else {
        return -1
    }
}

function kDiffCount(arr, k) {
    let count = 0
    arr = arr.sort((a,b)=>{
        return a-b
    })
    for(let i=0; i<arr.length-2; i++){
        if(binarySearch(arr,i+1,arr.length-1,arr[i]+k) != -1){
            count++
        }
    }
    return count
}

let arr = [1, 5, 3, 4, 2]
console.log(kDiffCount(arr, 3));