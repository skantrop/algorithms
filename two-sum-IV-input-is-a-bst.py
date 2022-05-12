# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findTarget(self, root, k):
        arr = []
        def bst_to_array(root): # recursive function()
            if not root:
                return
            bst_to_array(root.left)
            arr.append(root.val)
            bst_to_array(root.right)
        
        bst_to_array(root)  # we get array of all elements in bst
        for i in arr: 
            if k-i in arr and k-i!= i:
                return True
        return False
