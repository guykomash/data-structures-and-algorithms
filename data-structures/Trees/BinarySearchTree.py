import displayTree
class TreeNode:
    def __init__(self,value) -> None:
        self.left = self.right = None
        self.value = value

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, x):
        if not self.root:
            self.root = TreeNode(x)
            return
        self._insert(self.root, x)

    def _insert(self, root, x):
        if not root: return

        if x <= root.value:
            if not root.left:
                root.left = TreeNode(x)
                return
            else:
                self._insert(root.left, x)
                return
        else:
            if not root.right:
                root.right = TreeNode(x)
            else: self._insert(root.right, x)

    def search(self, x):
        self._search(self.root, x)

    def _search(self, root, x):
        if not root: return None

        if root.value == x:
            return root
        
        if x <= root.value:
            return self._search(root.left, x)
        else:
            return self._search(root.right,x )
    
    def delete(self, x):
        '''
        there are three cases:
        1. node is leaf:
        2. node has single child
        3. node has two children

        '''

        self.root = self._delete(self.root, x)

    def _delete(self, cur, x):
        if not cur: return
        # print(cur.value)
        if cur.value == x:

            # if cur is leaf, return None
            # if no right child, return the left child
            # if no left child return right child
            if not cur.left:
                return cur.right
            elif not cur.right:
                return cur.left

            # cur has two children. find the min in the right subtree and make him cur.
            successor  = cur.right
            while successor.left:
                successor = successor.left
            cur.value = successor.value
            cur.right = self._delete(cur.right, cur.value)
            return cur
        
        elif x < cur.value:
            cur.left = self._delete(cur.left, x)
        else: # x > cur.value
            cur.right = self._delete(cur.right, x)
        return cur
    
    def inOrder(self):
        inorder = self._inorder(self.root)
        return inorder

    def _inorder(self, root, stack=[]):
        if not root: return

        self._inorder(root.left,stack)
        stack.append(root.value)
        self._inorder(root.right, stack)
        return stack

    def preOrder(self):
        preorder = self._preorder(self.root)
        return preorder
    
    def _preorder(self,root, stack=[]):
        if not root: return

        stack.append(root.value)
        self._preorder(root.left,stack)
        self._preorder(root.right,stack)
        return stack
    
    
if __name__ == "__main__":
    bst = BST()
    bst.insert(3)
    bst.insert(1)
    bst.insert(2)
    bst.insert(5)
    bst.insert(4)
    print('\n')
    displayTree.display_tree(bst.root)
    inorder = bst.inOrder()
    print(inorder)
    preorder = bst.preOrder()
    print(preorder)    
    
    bst.delete(2)
    print('\n')
    displayTree.display_tree(bst.root)
    bst.delete(3)
    print('\n')
    displayTree.display_tree(bst.root)
