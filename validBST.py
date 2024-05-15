# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        else:
            #1 or mode nodes
            def privateMaxDepth(self, cur: Optional[TreeNode], minVal, maxVal):
                #print(cur)
                #print("min: " + str(minVal))
                #print("max: " + str(maxVal))
                
                #First, check if the current node is a binary search tree with it's children
                if cur.left == None and cur.right == None:
                    #print("leaf")
                    pass
                    
                else:
                    #print("internal")
                    
                    #Check left
                    if cur.left != None and cur.left.val < cur.val:
                        #print("pass 1")
                        pass
                    else:
                        if cur.left == None:
                            #print("no left child")
                            pass
                        else:
                            #print("left child greater than or equal to current")
                            return False

                    #Check right
                    if cur.right != None and cur.right.val > cur.val:
                        #print("pass 2")
                        pass
                    else:
                        if cur.right == None:
                            #print("no right child")
                            pass
                        else:
                            #print("right child less than or equal to current")
                            return False
                    
                
                #Second, check if the current node fits in to the overall BST
                if (minVal == None or cur.val > minVal) and (maxVal == None or cur.val < maxVal):
                    #print("pass 3")
                    pass
                else:
                    #print("cur.val is wrong")
                    return False
                
                
                #Go down the tree
                resultLeft = True
                resultRight = True
                
                if cur.left != None:
                    #print("going left")
                    resultLeft = privateMaxDepth(self, cur.left, minVal, cur.val)
                    
                else:
                    #print("no left child")
                    pass
                    
                if cur.right != None:
                    #print("going right")
                    resultRight = privateMaxDepth(self, cur.right, cur.val, maxVal)
                    
                else:
                    #print("no right child")
                    pass
                
                
                #Determine what to return coming back up the tree
                if resultLeft == False or resultRight == False:
                    return False
                else:
                    return True
                
                
            result = privateMaxDepth(self, root, None, None)  
            return result