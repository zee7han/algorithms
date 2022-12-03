function islandCount(grid){
    let count = 0
    let visited = new Set()

    for(let i=0; i<grid.length; i++){
        for(let j=0; j<grid[0].length; j++){
            if(explore(i,j,visited,grid) == true){
                count++  
            }
        }
    }
    return count
}


function explore(i, j, visited, grid) {
    let rowInbounds = (i >= 0 && i < grid.length)
    let colInbounds = (j >= 0 && j < grid.length)
    if(!rowInbounds || !colInbounds){
        return false
    }
    if(grid[i][j] == "0") {
        return false
    }

    let pos = `${i},${j}`
    if(visited.has(pos)){
        return false
    }
    visited.add(pos)

    explore(i-1, j, visited, grid)
    explore(i+1, j, visited, grid)
    explore(i, j-1, visited, grid)
    explore(i, j+1, visited, grid)

    return true
}

let grid = [["1","1","1","0","0"],["1","1","0","0","0"],["1","1","0","0","0"],["0","0","0","1","1"]]

console.log(islandCount(grid))