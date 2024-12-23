class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def isValidBst(node, prev):
    if node is None:
        return True
    
    # Check the left subtree
    if not isValidBst(node.left, prev):
        return False
    
    # Check current node value against the previous node's value
    if prev[0] is not None and prev[0] >= node.data:
        return False
    
    # Update the previous node's value
    prev[0] = node.data
    
    # Check the right subtree
    return isValidBst(node.right, prev)

def isBST(root):
    # Using a list to simulate pass-by-reference
    prev = [None]  
    return isValidBst(root, prev)

if __name__ == '__main__':
  
    # Create a sample binary tree
    #      4
    #    /   \
    #   2     5
    #  / \
    # 1   3

    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    if isBST(root):
        print("True")
    else:
        print("False")