function groupAnagram(arr){
    let groupMap = {}
    arr.forEach(element => {
        let sortedKey = element.split("").sort((a, b) => {{
            if (a > b) {
                return -1;
            }
            if (b > a) {
                return 1;
            }
            return 0;
        }}).join("")
        if(groupMap.hasOwnProperty(sortedKey)){
            groupMap[sortedKey].push(element)
        } else {
            groupMap[sortedKey] = [element]
        }
    });
    return Object.values(groupMap)
}

console.log(groupAnagram(["eat","tea","tan","ate","nat","bat"]))