# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        
        
        #Use breadth-first search for this
        q = Queue(maxsize = 0)
        q.put(root)
        #print("Empty: ", q.empty()) 
        
        root = True
        searching = True
        while(searching):
            if q.qsize() == 0:
                return True
            
            #If this is the root node
            elif q.qsize() == 1:
                #print("root node")
                nodeOne = q.get()
                nodeTwo = nodeOne
                
            #not the root node
            else:
                nodeOne = q.get()
                nodeTwo = q.get()
                
            #print(nodeOne)
            #print(nodeTwo)
            
            #if nodeOne has a left and/or right child
            if nodeOne.left != None or nodeOne.right != None:
                #Check if nodeTwo contains the mirrored child
                if nodeOne.left != None:
                    if nodeTwo.right != None:
                        #check if the values are the same
                        if nodeOne.left.val != nodeTwo.right.val:
                            return False
                    else:
                        return False
                
                if nodeOne.right != None:
                    if nodeTwo.left != None:
                        #check if the values are the same
                        if nodeOne.right.val != nodeTwo.left.val:
                            return False
                    else:
                        return False
                    
            #if nodeTwo has a left and/or right child
            if nodeTwo.left != None or nodeTwo.right != None:
                #Check if nodeOne contains the mirrored child
                if nodeTwo.left != None:
                    if nodeOne.right != None:
                        #check if the values are the same
                        if nodeTwo.left.val != nodeOne.right.val:
                            return False
                    else:
                        return False
                
                if nodeTwo.right != None:
                    if nodeOne.left != None:
                        #check if the values are the same
                        if nodeTwo.right.val != nodeOne.left.val:
                            return False
                    else:
                        return False
                    
            #print("current nodes are symetric")
            
            #Enqueue more nodes
            #If this is the root node
            if root == True:
                root = False
                #print("root node 2")
                if nodeOne.left != None and nodeOne.right != None:
                    q.put(nodeOne.left)
                    q.put(nodeOne.right)
                
            #not the root node
            else:
                #print("enqueue none root")
                #when enqueueing the nodes will be stored as  ...  3, 3', 4, 4' ...
                #so then when it pops off the next 2 elements they will be the nodes that should be compared 
                #against eachother
                
                #Don't enqueue Null nodes
                if nodeOne.left != None and nodeTwo.right != None:
                    q.put(nodeOne.left)
                    q.put(nodeTwo.right)
                    
                if nodeOne.right != None and nodeTwo.left != None:
                    q.put(nodeOne.right)
                    q.put(nodeTwo.left)
            
            #searching = False