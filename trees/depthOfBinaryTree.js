class Node {
    constructor(value, left, right){
        this.value = value
        this.left = left
        this.right = right
    }
}

// Using DFS
function depthOfBinaryTree(rootNode){
    if(rootNode == null){
        return 0
    }

    return 1 + Math.max(depthOfBinaryTree(rootNode.left),depthOfBinaryTree(rootNode.right))
}

//Using iterative DFS
function depthByBFS(rootNode){
    let stack = [[rootNode, 1]]
    let res = 0

    while(stack.length != 0){
        let [node, depth] = stack.pop()

        if(node != null){
            stack.push([rootNode.left, depth+1])
            stack.push([rootNode.right, depth+1])
            res = Math.max(res, depth)
        }
    }
    return res
}