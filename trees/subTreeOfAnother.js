function isSubtree(root, subTreeRoot){
    if(subTreeRoot == null){
        return true
    } else if(root == null){
        return false
    } else {
        if(isSameTree(root, subTreeRoot)){
            return true
        } else {
            return isSubtree(root.left, subTreeRoot) || isSubtree(root.right, subTreeRoot)
        }
    }
}


function isSameTree(root, subTreeRoot){
    if(root == null && subTreeRoot == null){
        return true
    } else {
        if(root.value == subTreeRoot.value){
            return isSameTree(root.left, subTreeRoot.left) && isSameTree(root.right, subTreeRoot.right)
        } else {
            return false
        }
    }
}