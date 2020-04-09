def maxPathSum(tree):
    _ , ans = findMaxSum(tree)
    return ans

def findMaxSum(tree):
    if tree is None:
        return (0,0)

    leftMaxSumBrunch, leftMaxSumPath = findMaxSum(tree.left)
    rightMaxSumBrunch, rightMaxSumPath = findMaxSum(tree.right)
    maxChildSumBrunch = max(leftMaxSumBrunch, rightMaxSumBrunch)

    value = tree.value
    maxSumAsBrunch = max(value, maxChildSumBrunch+value)
    maxSumAsRootNode = max(leftMaxSumBrunch+value+rightMaxSumBrunch, maxSumAsBrunch)
    maxPathSum = max(leftMaxSumPath, rightMaxSumPath, maxSumAsRootNode)

    return (maxSumAsBrunch, maxPathSum)
