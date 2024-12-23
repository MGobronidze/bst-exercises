# Python program to convert sorted 
# array to BST.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Recursive function to construct BST
def sortedArrayToBSTRecur(arr, start, end):
    if start > end:
        return None

    # Find the middle element
    mid = start + (end - start) // 2

    # Create root node
    root = Node(arr[mid])

    # Create left subtree
    root.left = sortedArrayToBSTRecur(arr, start, mid - 1)

    # Create right subtree
    root.right = sortedArrayToBSTRecur(arr, mid + 1, end)

    return root

def sortedArrayToBST(arr):
    return sortedArrayToBSTRecur(arr, 0, len(arr) - 1)

def preOrder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preOrder(root.left)
    preOrder(root.right)

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    root = sortedArrayToBST(arr)
    preOrder(root)