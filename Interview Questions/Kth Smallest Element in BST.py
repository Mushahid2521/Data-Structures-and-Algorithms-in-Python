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
            self.root = node

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



    def kthElement(self,kth):
        self.cnt = 0
        self.val = 0
        def inorderTraversal(root):
            if root:
                inorderTraversal(root.left)
                self.cnt+=1
                if self.cnt==kth:
                    self.val = root.key
                inorderTraversal(root.right)

        inorderTraversal(self.root)
        return self.val



bs = BST(Node(3))
bs.insert_it(Node(1))
bs.insert_it(Node(4))
bs.insert_it(Node(2))
bs.insert_it(Node(8))
bs.insert_it(Node(7))

print(bs.kthElement(2))