# Tree_sort algorithm
# Build a BST and in order traverse.
from segments.binary_tree.binary_tree import BinaryTree


class SortTree(BinaryTree):
    # BST data structure
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        super(SortTree, self).__init__()

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left == None:
                    self.left = SortTree(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right == None:
                    self.right = SortTree(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val


def inorder(root, res):
    # Recursive travesal
    if root:
        inorder(root.left, res)
        res.append(root.val)
        inorder(root.right, res)


def treesort(arr):
    # Build BST
    if len(arr) == 0:
        return arr
    root = SortTree(arr[0])
    for i in range(1, len(arr)):
        root.insert(arr[i])
    # Traverse BST in order.
    res = []
    inorder(root, res)
    return res


print(treesort([10, 1, 3, 2, 9, 14, 13]))
