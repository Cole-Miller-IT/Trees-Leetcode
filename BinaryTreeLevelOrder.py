# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        else: #1 or more nodes in the tree
            #Use breadth-first search for this
            q = Queue(maxsize = 0)
            q.put(root)
            #print("Empty: ", q.empty()) 
            currentCount = 1
            nextCount = 0
            tree = []
            currentLevel = []

            #While traversing the tree
            searching = True
            while(searching):
                currentNode = q.get()
                currentLevel.append(currentNode.val)
                currentCount -= 1
                
                #left first for order
                if currentNode.left != None:
                    nextCount += 1
                    q.put(currentNode.left)

                if currentNode.right != None:
                    nextCount += 1
                    q.put(currentNode.right)

                    
                if q.empty():
                    tree.append(currentLevel)
                    searching = False
                    break

                    
                if currentCount == 0:
                    tree.append(currentLevel)
                    currentLevel = []
                    currentCount = nextCount
                    nextCount = 0

                    
                
        return tree