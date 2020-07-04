# Python program to find sum of all paths from root to leaves

# A Binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Returs sums of all root to leaf paths. The first parameter is root
# of current subtree, the second paramete"r is value of the number
# formed by nodes from root to this node
def treePathsSumUtil(root, val):
    # Base Case
    if root is None:
        return 0

    # Update val
    val = (val * 10 + root.data)

    # If current node is leaf, return the current value of val
    if root.left is None and root.right is None:
        return val

    # Recur sum of values for left and right subtree
    return (treePathsSumUtil(root.left, val) +
            treePathsSumUtil(root.right, val))


# A wrapper function over treePathSumUtil()
def treePathsSum(root):
    # Pass the initial value as 0 as ther is nothing above root
    return treePathsSumUtil(root, 0)


# Driver function to test above function
root = Node(6)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(5)
root.right.right = Node(4)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
print("Sum of all paths is", treePathsSum(root))

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
