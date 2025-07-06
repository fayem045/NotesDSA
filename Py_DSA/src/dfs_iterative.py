from binary_search_tree import BinarySearchTree

# O(n)
# put uderscore - means private
# example: preorder_generator -> _preorder_generator
#doublee __ means cant access outside
class DFSIterative:
    def __init__(self, bst):#use binarysearchtree para d ulit ulit
        self.bst = bst
#generator first -optional
    def preorder_traversal(self):
        return self._preorder_generator() #generator

    def _preorder_generator(self):
        if self.bst.root is None: #ask muna: if no root
            return#return means empty root
        stack = [self.bst.root]
        while stack: #if d empty stack
            node = stack.pop()
            yield node.value #yield -basically return a value. it return value of node
            if node.right:
                 stack.append(node.right)#append in the right
            if node.left: #if not
                stack.append(node.left)

    def inorder_traversal(self):
        return self._inorder_generator()

    def _inorder_generator(self):
        stack = []
        current = self.bst.root
        while stack or current: #while may laman
            if current: #if may laman din
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                yield current.value
                current = current.right

    def postorder_traversal(self):
        return self._postorder_generator() #generator (optional)

    def _postorder_generator(self):
        if self.bst.root is None:
            return
        stack1 = [self.bst.root]
        stack2 = [] #empty lang
        while stack1:
            node = stack1.pop() #pop laman
            stack2.append(node) #pop and append. node lang kasi or laman
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            node = stack2.pop()
            yield node.value

def main() -> None:
    bst = BinarySearchTree()  # automatic import
    elements = [50, 30, 20, 40, 70, 60, 80]
    for element in elements:  # to insert in tree
        bst.add(element)

    dfs_recur = DFSIterative(bst)
    print("DFS Recursive - Pre-Order Traversal: ", list(dfs_recur.preorder_traversal()))
    print("DFS Recursive - In-Order Traversal: ", list(dfs_recur.inorder_traversal()))
    print("DFS Recursive - Post-Order Traversal: ", list(dfs_recur.postorder_traversal()))

if __name__ == '__main__':
    main()