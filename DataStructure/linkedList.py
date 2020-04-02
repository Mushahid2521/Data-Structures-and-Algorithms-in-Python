class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

    def traverse(self):
        node = self
        while node!=None:
            print(node.val)
            node = node.next

    def printnext(self):
        print(self.next)


def deleteNodeNext(nthNode, node):
    nthNode.next = node.next

def sumTwoList(head1, head2):
    sum1 = ""
    node = head1
    while node!=None:
        sum1+=str(node.val)
        node = node.next
    sum2 = ""
    node = head2
    while node!=None:
        sum2+=str(node.val)
        node = node.next
    return int(sum1)+int(sum2)



if __name__=='__main__':
    node1 = Node(12)
    node2 = Node(43)
    node3 = Node(56)
    node4 = Node(5)

    node5 = Node(4)
    node6 = Node(19)
    node7 = Node(88)

    node5.next = node6
    node6.next = node7

    node1.next = node2
    node2.next = node3
    node3.next = node4

    #node1.traverse()

    #deleteNodeNext(node1,node2)

    #node1.traverse()
    print(sumTwoList(node1, node5))

