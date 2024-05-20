# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        
        else:
            #1 or more values
            #Works be going through the array starting at the middle index and splitting up the array into left and right slices to build the tree (works b/c the array is in ascending order)
            def privateSortedArray(self, array: List[int], leftStartIndex, rightEndIndex):
                #print("---------------------------------")
                #print("array: " + str(array))

                #go to the middle value of the slice of the left and right array, take the greatest 
                #node either 1 (odd) or 2 (even) values to choose from

                #middleIndex = math.ceil(len(array) / 2)  #round up
                middleIndex = math.ceil((leftStartIndex + rightEndIndex) / 2)  #round up
                #print("middle value array: " + str(array[middleIndex]))

                #create the node
                newNode = TreeNode(val = array[middleIndex])
                #print(newNode)
                

                #everything to the left of the value in the array will be on the left side of the tree 
                #from this node and the same with the right side
                rightIndexStart = middleIndex + 1
                rightIndexEnd = rightEndIndex
                
                
                leftIndexStart = leftStartIndex
                leftIndexEnd = middleIndex - 1
                
                
                
                
                #if left slice not empty
                if leftIndexEnd >= leftIndexStart:
                    #call again recursively
                    #print("going Left")
                    #print("start left: " + str(leftIndexStart))
                    #print("end left: " + str(leftIndexEnd))
                    newNode.left = privateSortedArray(self, nums, leftIndexStart, leftIndexEnd)
                    
                #if right slice not empty
                if rightIndexStart <= rightIndexEnd:
                    #call again recursively
                    #print("going Right")
                    #print("start right: " + str(rightIndexStart))
                    #print("end right: " + str(rightIndexEnd))
                    newNode.right = privateSortedArray(self, nums, rightIndexStart, rightIndexEnd)
            
                #print("****************************************")
                #print("Node after coming back up")
                #print(newNode)
                return newNode
            
            #Start at the root
            root = privateSortedArray(self, nums, 0, len(nums) - 1)
            #print("Final tree")
            #print(root)
            return root
            