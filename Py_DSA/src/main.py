from binary_search_tree import BinarySearchTree
from dfs_iterative import DFSIterative
from bfs_traversal import BFSTraversal

def main() -> None:
    bst = BinarySearchTree() #automatic import
    elements = [50, 30, 20, 40, 70, 60, 80]
    for element in elements:# to insert in tree
        bst.add(element)

    #DFS Iterative
    #PRE-ORDER TRANSVERSAL= main root -> left all if no na -> right baba -> root ->left ->right
    dfs_iter = DFSIterative(bst)
    print("DFS Iterative- Pre-Order Traversal: ", list(dfs_iter.preorder_traversal()))
    print("DFS Iterative- In-Order Traversal: ", list(dfs_iter.inorder_traversal())) #left ->root ->right
    print("DFS Iterative- Post-Order Traversal: ", list(dfs_iter.postorder_traversal())) #left -> right - >root
    #dfs_iter._post.....# to prevent na access other generator sa iterative. PROTECTED, CAN ACCESS BUT MABIGYAN NG WARN
    #double __ hindi sya makita here

    #DFS RECURSIVE - mas madali
    dfs_recur = DFSIterative(bst)
    print("DFS Recursive - Pre-Order Traversal: ", list(dfs_recur.preorder_traversal()))
    print("DFS Recursive - In-Order Traversal: ", list(dfs_recur.inorder_traversal()))
    print("DFS Recursive - Post-Order Traversal: ", list(dfs_recur.postorder_traversal()))

    #BFS TRAVERSAL -need import din sa taas
    bfs_traver = BFSTraversal(bst)
    print("BFS Traversal: ", list(bfs_traver.bfs_traversal())) #func sa main/func sa file na kinukhanan

    print("Finding an Element: ", bst.__contains__(50))
    print("Finding an Element: ", 50 in bst)
    print("size of Tree: ", len(bst)) #pag d mahanap len or name ng func, check indention
    print("Height of TRee: ", bst.height())

    #copy of BST
    bst_copy = bst.copy()
    copy_dfs_iter = DFSIterative(bst_copy)
    print("In-Order Traversal Copy: ", list(copy_dfs_iter.inorder_traversal()))

if __name__ == '__main__':
    main()