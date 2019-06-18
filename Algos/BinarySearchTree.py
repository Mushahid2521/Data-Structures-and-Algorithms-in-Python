class Node():
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None


class BST():
    def __init__(self, root):
        self.root = root

    def insert_it(self, node):
        self.insert(self.root, node)

    def insert(self, root, node):
        if root == None:
            root = node

        else:
            if root.key < node.key:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right, node)

            else:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left, node)



    def inorderIt(self):
        self.inorder(self.root)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key)
            self.inorder(root.right)



if __name__=="__main__":
    bst = BST(Node(50))

    bst.insert_it(Node(30))
    bst.insert_it(Node(20))
    bst.insert_it(Node(40))
    bst.insert_it(Node(70))
    bst.insert_it(Node(60))
    bst.insert_it(Node(80))

    bst.inorderIt()

