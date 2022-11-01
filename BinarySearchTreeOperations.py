# Binary Search Tree operations in Python


# Create a node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Insert a node
def insert(node, key):

    # Return a new node if the tree is empty
    if not node:
        return Node(key)
    if node.key < key:
        node.right = insert(node.right,key)
    else:
        node.left = insert(node.left,key)

    return node

# # Inorder traversal
# def inOrder(root):
#     if root is not None:
#         # Traverse left
#         inOrder(root.left)
#
#         # Traverse root
#         print(str(root.key) + "->", end=' ')
#
#         # Traverse right
#         inOrder(root.right)
def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print(root.key,end=' ')
        inOrder(root.right)

def searchTree(root,data):
    if not root:
        return False
    if root.key == data:
        return True
    if root.key > data:
        return searchTree(root.right,data)
    else:
        return searchTree(root.left,data)
def minValue(root):
    if not root:
        return None
    if not root.left:
        return root.key
    cur = root
    while cur.left:
        cur = cur.left
    return cur.key
root = None
root = insert(root, 8)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 4)


inOrder(root)

print(searchTree(root,11))

print(minValue(root))