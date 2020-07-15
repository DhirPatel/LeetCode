# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkIfMirror(self, lst, rst):
        
        if lst is None and rst is None:
            return True
        
        if lst is not None and rst is not None and lst.val != rst.val:
            return False
        
        return (lst and rst) and self.checkIfMirror(lst.left, rst.right) and self.checkIfMirror(lst.right, rst.left)
    
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if root is None:
            return True
        
        #get left and right subtrees
        leftSubTree = root.left
        rightSubTree = root.right
        
        if self.checkIfMirror(leftSubTree, rightSubTree):
            return True
        else:
            return False