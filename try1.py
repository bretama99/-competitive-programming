class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, node):
        if self.head is None:
            self.head = node
        else:
            newNode = self.head
            while newNode.next:
                newNode = newNode.next
            newNode.next=node
    def display(self):
        newNode = self.head
        while newNode:
            print(newNode.data)
            newNode = newNode.next
    def insertAtBegining(self,node):
        node.next = self.head
        self.head = node

    def insertAtEnd(self,node):
        if self.head is None:
            self.head = node
        else:
            newNode = self.head
            while newNode.next:
                newNode = newNode.next
            newNode.next = node
    def insertAt(self,node,position):

        newNode = self.head
        count=0
        while newNode:
            if count == position:
                if position==0:
                    node.next = self.head
                    self.head = node
                else:
                    previousNode.next = node
                    node.next = newNode
                break
            previousNode = newNode
            newNode = newNode.next
            count+=1
        else:
            self.insertAtEnd(node)
    def length(self):
        node = self.head
        count =0
        while node:
            count+=1
            node = node.next
        print(count)
    def deleteNode(self):
        currentNode = self.head
        while currentNode.next:
            peviousNode = currentNode
            currentNode = currentNode.next
        peviousNode.next = None
        self.length()
    def deleteHead(self):
        currentNode = self.head
        self.head = currentNode.next
        # self.head=currentNode.next
        self.length()
        self.display()
    def deleteAt(self,position):
        currentNode = self.head
        count=0
        while currentNode.next:
            if count == position:
                previousNode.next = currentNode.next
                self.length()
                self.display()
                break
            previousNode = currentNode
            currentNode = currentNode.next
            count+=1
firstNode = Node("brhane")
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode = Node("tamrat")
linkedList.insert(secondNode)
thirdNode = Node("Gidey")
linkedList.insert(thirdNode)
fourthNode = Node("Sibhatu")
linkedList.insertAtBegining(fourthNode)
fivthNode = Node("Ghet")
linkedList.insertAtEnd(fivthNode)
sixNode = Node("Sinke")
linkedList.insertAt(sixNode,5)
linkedList.display()
linkedList.length()
linkedList.deleteNode()
linkedList.length()
linkedList.deleteHead()
linkedList.deleteAt(2)
