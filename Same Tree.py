# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, head, lst):
        if head == None:
            return
        lst.append(head)
        if head.left:
            self.traverse(head.left, lst)
        elif head.right:
            lst.append('null')
        if head.right:
            self.traverse(head.right, lst)
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_t = []
        self.traverse(p, p_t)
        q_t = []
        self.traverse(q, q_t)
        p_t = [x.val if type(x) == TreeNode else x for x in p_t]
        q_t = [x.val if type(x) == TreeNode else x for x in q_t]
        return p_t == q_t