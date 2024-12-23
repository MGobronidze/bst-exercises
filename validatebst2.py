class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# Helper function to check if a tree is
# BST within a given range
def isBstUtil(node, min_val, max_val):
    if node is None:
        return True

    # If the current node's data 
    # is not in the valid range, return false
    if node.data < min_val or node.data > max_val:
        return False

    # Recursively check the left and 
    # right subtrees with updated ranges
    return (isBstUtil(node.left, min_val, node.data - 1) and
            isBstUtil(node.right, node.data + 1, max_val))

# Function to check if the entire binary tree is a BST
def isBST(root):
    return isBstUtil(root, float('-inf'), float('inf'))

if __name__ == "__main__":
  
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