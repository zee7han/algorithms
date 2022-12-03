function meetingRoomsRequired(intervals){
    let startTime = []
    let endTime = []
    intervals.forEach(el => {
        startTime.push(el.start)
        endTime.push(el.end)
    });
    startTime = startTime.sort((a,b)=>{return a-b})
    endTime = endTime.sort((a,b)=>{return a-b})

    let s = 0
    let e = 0
    let res = 0
    let meetingRoomsNeeded = 0

    while(s < intervals.length){
        if(startTime[s] < endTime[e]){
            s++
            meetingRoomsNeeded++
        } else {
            e++
            meetingRoomsNeeded--
        }
        res = Math.max(res, meetingRoomsNeeded)
    }

    return res
}