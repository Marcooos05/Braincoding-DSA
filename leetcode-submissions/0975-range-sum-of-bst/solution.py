# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        def recursion(node, low, high):
            if node == None:
                return 0
            elif node.val < low:
                return recursion(node.right, low, high)
            elif node.val > high:
                return recursion(node.left, low, high)
            else: #if node.val is within the range
                return  node.val + recursion(node.right, low, high) + recursion(node.left, low, high)
        return recursion(root, low, high)
        
