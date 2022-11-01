function longestConsecutiveSequenc(arr){
    let elementSet = new Set(arr)
    let longest = 0

    for(let i=0; i<arr.length; i++){
        if(!elementSet.has(arr[i]-1)){
            let lngth = 0
            while(elementSet.has(arr[i]+lngth)){
                lngth++
            }
            longest = Math.max(longest,lngth)
        }
    }
    return longest
}

console.log(longestConsecutiveSequenc([100,4,200,1,3,2]))