# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#It wants it a bit differently
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = None
        heightOfTree = 0
        
        #add all of the numbers to the tree
        for num in nums:
            #print(num)
            
            newNode = TreeNode()
            newNode.val = num
            
            temp = root
            root = newNode
            root.left = temp
            
            heightOfTree += 1
            #print(root)
          
        #print(root)
        #print(heightOfTree)
        #then starting at the root, move down the root node to the right child until the 
        #tree is height balanced within 1 height of difference
        maxHeight = heightOfTree
        balancing = True
        while(balancing):
            #print(root)
            #print(math.ceil((maxHeight / 2)))
            #round height up to an integer
            if heightOfTree > math.ceil((maxHeight / 2)):
                #balance the tree once
                newRoot = root.left
                newRoot.right = root
                root.left = None
                root = newRoot
                
                heightOfTree -= 1
                
            else:
                balancing = False
                break
            
            
        #print("final: " + str(root))
        return root
            