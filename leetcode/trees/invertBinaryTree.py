'''
226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
'''
from leetcode.trees.displayTree import display_tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root):
    if not root: return
    left = invertTree(root.left)
    right = invertTree(root.right)
    root.left = right
    root.right = left
    return root





if __name__ == "__main__":
    root = TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(7, TreeNode(6),TreeNode(9)))
    display_tree(root)
    root = invertTree(root)
    display_tree(root)
