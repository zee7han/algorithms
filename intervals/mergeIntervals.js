function mergeIntervals(intervals) {
    intervals = intervals.sort((a,b)=>{ return a[0] - b[0]})

    let res = [intervals[0]]

    for(let i=1; i<intervals.length; i++){
        if(res[res.length-1][1] >= intervals[i][0]){
            res[res.length-1][1] = Math.max(res[res.length-1][1], intervals[i][1])
        } else {
            res.push(intervals[i]) 
        }
    }
    return res
}


console.log(mergeIntervals([[1,4],[3,6],[20,100],[4,5]]))