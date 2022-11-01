function frequentElement(arr, k){
    let countMap = {}
    let freq = new Array(arr.length+1).fill([])
    arr.forEach(element => {
        countMap[element] ? countMap[element]++ : countMap[element]=1
    });
    Object.keys(countMap).forEach((it)=>{
        freq[countMap[it]] = [...freq[countMap[it]],parseInt(it)]
    })
    let res = []
    for(let i=freq.length-1; i>0; i--){
        for(n of freq[i]){
            res.push(n)
            if(res.length == k){
                return res
            }
        }
    }
}


console.log(frequentElement([1,1,2,2,2,1,3],2))