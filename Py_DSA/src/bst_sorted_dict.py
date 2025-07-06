from sortedcontainers import SortedDict
#lalagay ng key
class BinarySearchWithSortedDict:
    def __init__(self):
        self.bst = SortedDict()

    def insert(self, key, value):
        self.bst[key] = value

    def search(self, key):
        return key in self.bst

    def delete(self, key):
        if key in self.bst:
            del self.bst[key]

    def inorder_traversal(self):
        return list(self.bst.items())#insted of self.bst. = self.bst.items

    def size(self):
        return len(self.bst)

    def height(self):
        return self._height_helper(self.bst.keys())

    def _height_helper(self, keys): #use sortedMap
        if not keys:
            return -1 #Height of an empty tree is define as -1
        mid_index = len(keys) // 2
        left_subtree = keys[:mid_index]
        right_subtree = keys[mid_index + 1:]
        left_height = self._height_helper(left_subtree)
        right_height = self._height_helper(right_subtree)
        return 1 + max(left_height, right_height)

    def copy(self):
        new_bst = BinarySearchWithSortedDict()
        new_bst.bst = self.bst.copy()
        return new_bst

def main() -> None:
    bst = BinarySearchWithSortedDict()
    bst.insert(50, "Apple")
    bst.insert(30, "Banana")
    bst.insert(20, "Mango")
    bst.insert(40, "Orange")
    bst.insert(70, "Cherry")
    bst.insert(60, "Peach")
    bst.insert(80, "Plum")

    print("In-order Traversal: ",  bst.inorder_traversal())
    bst.delete(50)
    print("In-order Traversal: ",  bst.inorder_traversal())
    print("Height: ", bst.height())
    bst_copy = bst.copy()
    print("Copy In- Order Traversal: ", bst_copy.inorder_traversal())
    print("Search 30", bst.search(30))


if __name__ == '__main__':
    main()
