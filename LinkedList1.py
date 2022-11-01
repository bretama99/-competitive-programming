class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        newNode = self.head
        for _ in range(index):
            newNode = newNode.next
        return newNode.data

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
        newNode = self.head
        while newNode.next:
            newNode = newNode.next
        newNode.next = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if self.size <= index:
            return
        node = Node(val)
        newNode = self.head
        for _ in range(index):
            newNode = newNode.next
        node.next = newNode.next
        newNode.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        newNode = self.head
        prev = newNode
        while newNode.next:
            prev = newNode
            newNode = newNode.next
        prev.next = newNode.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)