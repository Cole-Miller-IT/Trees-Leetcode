# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            #Empty Tree
            return 0
        else:
            #Tree with 1 or more values
            def privateMaxDepth(self, cur: Optional[TreeNode], curDepth):
                #Move down the tree recursively
                leftDepth = curDepth
                rightDepth = curDepth
                
                if cur.left != None:
                    #go left
                    leftDepth = privateMaxDepth(self, cur.left, curDepth + 1)

                if cur.right != None:
                    #go right
                    rightDepth = privateMaxDepth(self, cur.right, curDepth + 1)
                     
                        
                #What to return back
                if leftDepth > rightDepth:
                    return leftDepth
                
                elif rightDepth > leftDepth:
                    return rightDepth
                
                else:
                    #Equal
                    return leftDepth
                
                
            depth = 1
            result = privateMaxDepth(self, root, depth)
            return result