function gasStation(gas, cost){
    let totalGas = gas.reduce((val, acc)=>{ return acc+val}, 0)
    let totalCost = cost.reduce((val, acc)=>{ return acc+val}, 0)

    if(totalGas < totalCost){
        return -1
    } else {
        let total = 0
        let start = 0
        for(let i=0; i<gas.length; i++){
            total += (gas[i]-cost[i])
            if(total < 0){
                total = 0
                start = i+1
            }
        }
        return start
    }

}