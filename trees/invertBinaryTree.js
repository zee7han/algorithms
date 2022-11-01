class Node {
    constructor(value, left, right){
        this.value = value
        this.left = left
        this.right = right
    }
}


function invertTree(rootNode){
    if(rootNode == null){
        return null
    }

    let tmp = rootNode.left
    rootNode.left = rootNode.right
    rootNode.right = tmp
    invertTree(rootNode.left)
    invertTree(rootNode.right)
    return rootNode

}