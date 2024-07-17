'''
235. Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

'''

from leetcode.trees.displayTree import display_tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    p = p.val
    q = q.val
    if p > q:
        p, q = q, p
    
    print(f"LCA Called, p = {p}, q = {q}")

    # the idea here is to find a node where p <= node <= q?
    while root:
        if root.val > p and root.val > q:
            root = root.left
        elif root.val < p and root.val < q:
            root = root.right
        else:
            break

    if root: print(f"LCA = {root.val}")
    return root


if __name__ == "__main__":
    root = TreeNode(6,TreeNode(2,TreeNode(0),TreeNode(4)),TreeNode(8, TreeNode(7),TreeNode(9)))
    display_tree(root)
    lowestCommonAncestor(root,TreeNode(2), TreeNode(4))