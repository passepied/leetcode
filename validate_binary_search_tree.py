# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.isValidBSTrec(root, float("-infinity"),float("infinity"))
        
    def isValidBSTrec(self, root, min, max):
        if root== None:
            return True
        if root.val<=min or root.val>=max:
            return False
        solution = self.isValidBSTrec(root.left, min, root.val)
        solution = solution and self.isValidBSTrec(root.right, root.val, max)
        return solution