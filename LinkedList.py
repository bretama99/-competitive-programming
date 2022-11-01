class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,data):
        node = Node(data)
        if self.head==None:
            self.head=node
        else:
            newNode = self.head
            while newNode.next:
                newNode = newNode.next
            newNode.next = node
    def insertFirst(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
    def insertAtP(self,position,data):
        node = Node(data)
        newNode = self.head
        for i in range(1,position):
           if newNode.next:
               newNode = newNode.next
        node.next = newNode.next
        newNode.next = node
    def deleteFirst(self):
        self.head = self.head.next
    def deleteEnd(self):
        node = self.head
        while node.next.next:
            node = node.next
        node.next = None
    def deleteM(self,p):
        node = self.head
        for i in range(1,p):
            if node.next:
                node=node.next
        node.next = node.next.next
    def searchKey(self,key):
        node = self.head
        while node:
            if node.data == key:
                return True
            node = node.next
        return False

    def sortList(self):
        current = self.head
        while current:
            index = current.next
            while index:
                if current.data>index.data:
                    current.data,index.data = index.data,current.data
                index = index.next
            current = current.next

linkedList = LinkedList()

linkedList.insert(7)
linkedList.insert(6)
linkedList.insert(5)
linkedList.insert(1)
# linkedList.insertFirst(10)
# linkedList.insertAtP(2,0)
# linkedList.deleteFirst()
# linkedList.deleteEnd()
# linkedList.deleteM(2)
# print(linkedList.searchKey(5))
linkedList.sortList()
while linkedList.head:
    print(linkedList.head.data)
    linkedList.head = linkedList.head.next
