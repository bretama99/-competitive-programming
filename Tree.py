class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
def preOrder(root):
    if root:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data)
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.left = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
preOrder(root)
postOrder(root)
inOrder(root)