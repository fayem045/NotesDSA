from tree_node import TreeNode

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0 #for sie sa len

    #insert a value
    def add(self, value):
        #ask muna
        if self.root is None:#if blanko
            self.root = TreeNode(value)
            self.size += 1 #add this too para sa size sa len
            return
        #if not empty
        self._insert_rec(self.root, value)

    def _insert_rec(self, node, value):#adding put also in maind
        if node is None:
            self.size += 1
            return TreeNode(value)
        if value < node.value:
            node.left = self._insert_rec(node.left, value)
        elif value > node.value:
            node.right = self._insert_rec(node.right, value)
        return node #sa labas kasi return sya after for both sides not lang isa

    #find value
    def __contains__(self, value):
        return self._search_rec(self.root, value)

    def _search_rec(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_rec(node.left, value)
        elif value > node.value:
            return self._search_rec(node.right, value) #traverse on the right

     #check size
    def __len__(self):
        return self.size

    #get height
    def height(self):
        return self._height_helper(self.root)

    def _height_helper(self, node):
        if node is None:
            return -1 #Height of an empty tree is define as -1
        left_height = self._height_helper(node.left)
        right_height = self._height_helper(node.right)
        return 1 + max(left_height, right_height) #tiganna mas malaki and plus 1

    def copy(self):
        new_bst = BinarySearchTree()
        new_bst.root = self._copy_helper(self.root)
        new_bst.size = self.size
        return new_bst

    def _copy_helper(self, node):
        if node is None:
            return None
        # if not none, return preorder traversal caue pop it
        new_node = TreeNode(node.value)
        new_node.left = self._copy_helper(node.left)
        new_node.right = self._copy_helper(node.right)
        return new_node



