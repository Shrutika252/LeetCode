
#class TreeNode:
#def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder=[]
        if root:
            inorder=self.inorderTraversal(root.left)
            inorder.append(root.val)
            inorder=inorder+self.inorderTraversal(root.right)
        
        return inorder
        