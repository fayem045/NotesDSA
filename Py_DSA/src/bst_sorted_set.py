from sortedcontainers import SortedSet

class BinarySearchWithSortedSet:
    def __init__(self):
        self.bst = SortedSet()

    def insert(self, value):
        self.bst.add(value)

    def search(self, value):
        return value in self.bst

    def delete(self, value):
        return self.bst.discard(value)

    def inorder_traversal(self):
        return list(self.bst)

    def size(self):
        return len(self.bst)

    def height(self):
        return self._height_helper(self.bst)

    def _height_helper(self, sorted_set):
        if not sorted_set:
            return -1 #Height of an empty tree is define as -1
        mid_index = len(sorted_set) // 2
        left_subtree = sorted_set[:mid_index]
        right_subtree = sorted_set[mid_index + 1:]
        left_height = self._height_helper(left_subtree)
        right_height = self._height_helper(right_subtree)
        return 1 + max(left_height, right_height)

    def copy(self):
        new_bst = BinarySearchWithSortedSet()
        new_bst.bst = self.bst.copy()
        return new_bst

def main() -> None:
    bst = BinarySearchWithSortedSet()
    elements =[50,40,30,20,10,-10]
    for element in elements:  # to insert in tree
     bst.insert(element)
    print("In-order Traversal: ",  bst.inorder_traversal())
    bst.delete(50)
    print("In-order Traversal: ",  bst.inorder_traversal())
    print("Height: ", bst.height())
    bst_copy = bst.copy()
    print("Copy In- Order Traversal: ", bst_copy.inorder_traversal())
    print("Search 30", bst.search(30))


if __name__ == '__main__':
    main()
