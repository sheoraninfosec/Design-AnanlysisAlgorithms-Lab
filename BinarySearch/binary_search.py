# Author: Jigesh Sheoran
# SAP ID: 590025428

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

# preorder (root → left → right)
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# inorder (left → root → right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# postorder (left → right → root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

values = list(map(int, input("Enter numbers separated by space: ").split()))

root = None
for v in values:
    root = insert(root, v)

print("\nPreorder Traversal:", end=" ")
preorder(root)

print("\nInorder Traversal:", end=" ")
inorder(root)

print("\nPostorder Traversal:", end=" ")
postorder(root)

