function platformNeeded(arrival, depart, n) {
    arrival = arrival.sort()
    depart = depart.sort()

    let result = 1
    let plat_needed = 1
    let i = 1
    let j = 0

    while(i < n && j < n){
        if(arrival[i] < depart[j]){
            plat_needed++
            i++
        } else if (arrival[i] > depart[j]){
            plat_needed--
            j++
        }

        if(plat_needed > result){
            result = plat_needed
        }
    }
    return result
}

let arr = [900, 940, 950, 1100, 1500, 1800]
let dep = [910, 1200, 1120, 1130, 1900, 2000]
let n = arr.length

console.log(platformNeeded(arr, dep, n));