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

    def removeKfromList(self, head, key):
        temp = head
        prev = None

        # Check if the head contains the key repeatedly
        while temp!=None and temp.val==key:
            head = temp.next
            temp = temp.next

        while temp!=None:
            # Search for the key to be deleted,
            # keep track of the previous node
            # as we need to change 'prev.next'
            while temp!=None and temp.val != key:
                prev = temp
                temp = temp.next

            # If there is no element equal to Key
            if temp==None:
                return head

            # We got an key, so unlink it
            prev.next = temp.next

            # Update temp for next iteration for outer loop
            temp = prev.next

        return head






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
    node5 = Node(56)

    node6 = Node(19)
    node7 = Node(88)

    # node5.next = node6
    # node6.next = node7

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    node1.traverse()
    node1.removeKfromList(node1, 56)
    node1.traverse()

    # nodep1 = Node(1000)
    # nodep2 = Node(1000)
    # nodep1.next = nodep2
    # #
    # nodep1.traverse()
    # nodep1.removeKfromList(nodep1, 1000)
    # print()
    # nodep1.traverse()

    #deleteNodeNext(node1,node2)

    #node1.traverse()
    #print(sumTwoList(node1, node5))

