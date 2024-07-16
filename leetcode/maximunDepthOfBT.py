'''
104. Maximun Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

'''

from displayTree import display_tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    if not root: return 0

    left = maxDepth(root.left)
    right = maxDepth(root.right)

    return max(left, right)  + 1




if __name__ == "__main__":
    root = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
    display_tree(root)
    print(maxDepth(root))
