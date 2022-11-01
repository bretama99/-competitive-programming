from try1 import LinkedList, Node
def mergeList(linkedList1,linkedList2,mergedList):
    currentfirst = linkedList1.head
    currentSecond = linkedList2.head
    while True:
        if currentfirst is None:
            mergedList.insert(currentSecond)
            break
        if currentSecond is None:
            mergedList.insert(currentfirst)
        if currentfirst.data<currentSecond.data:
            currentfirstNext = currentfirst.next
            currentfirst.next = None
            mergedList.insert(currentfirst)
            currentfirst = currentfirstNext
        else:
            currentSecondNext = currentSecond.next
            currentSecond.next = None
            mergedList.insert(currentSecond)
            currentSecond = currentSecondNext


node1 = Node(1)
node2 = Node(3)
node3 = Node(4)
linkedList1 = LinkedList()
linkedList1.insert(node1)
linkedList1.insert(node2)
linkedList1.insert(node3)

node4 = Node(2)
node5 = Node(5)
node6 = Node(7)
linkedList2 = LinkedList()
linkedList2.insert(node4)
linkedList2.insert(node5)
linkedList2.insert(node6)
linkedList1.display()
linkedList2.display()
mergedList = LinkedList()
mergeList(linkedList1,linkedList2,mergedList)
