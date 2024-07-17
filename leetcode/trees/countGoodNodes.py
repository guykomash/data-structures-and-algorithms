'''
1448. Count Good Nodes in Binary Tree
https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

'''





from displayTree import display_tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def goodNodes(root):
    
    def _goodNodes(root, greatest):
        if not root: 
            return 0

        rootScore = 0
        if root.val >= greatest:
            rootScore += 1
            greatest = root.val

        right = _goodNodes(root.right, greatest)
        left = _goodNodes(root.left, greatest)
        
        return rootScore + right + left
    
    return _goodNodes(root, root.val)




if __name__ == "__main__":
    root = TreeNode(3,TreeNode(1,TreeNode(3)),TreeNode(4, TreeNode(1),TreeNode(5)))
    display_tree(root)