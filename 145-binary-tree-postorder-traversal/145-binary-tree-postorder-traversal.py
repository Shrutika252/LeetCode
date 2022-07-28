# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        post=[]
        if root:
           
            post=self.postorderTraversal(root.left)
            post=post+self.postorderTraversal(root.right)
            post.append(root.val)
        
        return post