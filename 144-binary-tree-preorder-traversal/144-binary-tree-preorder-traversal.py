# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pre=[]
        if root:
           
            pre.append(root.val)
            pre=pre+self.preorderTraversal(root.left)
            pre=pre+self.preorderTraversal(root.right)
        
        return pre