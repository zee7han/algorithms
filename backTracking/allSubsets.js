function allSubsets(arr){
    let output = []
    let subsets = []

    dfs(0,arr,output,subsets)

    return output
    
}


function dfs(i,arr,output,subsets) {
    if(i >= arr.length){
        output.push(JSON.stringify(subsets))
        return
    }

    subsets.push(arr[i])
    dfs(i+1,arr,output,subsets)

    subsets.pop()
    dfs(i+1,arr,output,subsets)
}



console.log(allSubsets([1,2,3]))