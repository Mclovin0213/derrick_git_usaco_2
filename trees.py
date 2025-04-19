class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node('FPE:S')
root.left = Node('RC2')
root.right = Node('Deadline')
root.left.left = Node('Grace')
root.left.right = Node('Bombline')
root.right.left = Node('Doors')
root.right.right = Node('JTOH XL')

def pre_order(node):
    if node:
        print(node.data, end = ' ')
        pre_order(node.left)
        pre_order(node.right)

print("Pre-order Traversal")
pre_order(root)

def in_order(node):
    if node:
        in_order(node.left)
        print(node.data, end = ' ')
        in_order(node.right)

print("\nIn-order Traversal")
in_order(root)

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end = ' ')

print("\nPost-order Traversal")
post_order(root)