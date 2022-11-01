class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
class Tree:
    def createNode(self,data):
        return Node(data)
    def insert(self,node,data):
        if not node:
            return self.createNode(data)
        if node.data < data:
            node.right = self.insert(node.right,data)
        else:
            node.left = self.insert(node.left,data)
        return node
    def inorder(self,root):
        if not root:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)
tree = Tree()
root = tree.createNode(5)
tree.insert(root,2)
tree.insert(root,10)
tree.insert(root,7)
tree.insert(root,15)
tree.insert(root,12)
tree.insert(root,20)
tree.insert(root,30)
tree.insert(root,6)
tree.insert(root,8)

print("=======inorder traversal=========")
tree.inorder(root)