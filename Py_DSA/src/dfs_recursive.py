#o(n)
#problem mahihar pag may stock overflow
class DFSRecursive:
    def __init__(self, bst):
        self.bst = bst

    def preorder_traversal(self):
        return self._preorder_generator(self.bst.root) #return generator

    def _preorder_generator(self, node):
        if node:
            yield node.value
            yield from self._preorder_generator(node.left)
            yield from self._preorder_generator(node.right)#then right

    def inorder_traversal(self):
        return self._inorder_generator(self.bst.root)

    def _inorder_generator(self, node): #left -> root -> right = kaya baligtarin lang places neto
        if node:
            yield from self._inorder_generator(node.left)
            yield node.value
            yield from self._inorder_generator(node.right)

    def post_order_traversal(self):
        return self._postorder_generator(self.bst.root)

    def _postorder_generator(self, node): #left -> right -> root
        if node:
            yield from self._inorder_generator(node.left)
            yield from self._inorder_generator(node.right)
            yield node.value