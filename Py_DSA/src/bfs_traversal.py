class BFSTraversal:
    def __init__(self, bst): #bst-define func
        self.bst = bst

    def bfs_traversal(self): #create a func
        return self._bfs_generator()

    def _bfs_generator(self):
        if self.bst.root is None:
            return
        #if not empty
        queue = [self.bst.root]
        while queue:
            node = queue.pop(0)
            yield node.value
            if node.left: #ask if may value sa left
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

