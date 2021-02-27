# Problem Statement : https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/
# Definition for a binary tree node.

# Python program to print level 
# order traversal using Queue
# A node structure

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Assumption: Complete binary tree, get level number from counter
          (1)
    (2)         (3)
(4)           (6)  (7)


'''
def levelOrder(root: TreeNode) -> List[List[int]]: # root = (1)
    if root is None: # (1) is None?
        return
    
    levels = [] # [[1],[2,3], []]
    level_counter = 0 # 2
    
    q = [] # [4,6,7,none]
    q.append(root)
    q.append(None)
    levels.append([]) #
    while(len(q) > 0): # len(q) == 4
        n = q.pop(0) # n = none
        if n is None:
            if len(q) > 0:
                level_counter += 1
                levels.append([])
                q.append(None) # adding delimiter to indicate end of level
            continue
        
        levels[level_counter].append(n.val) # levels[1].append(3)
        if n.left is not None:
            q.append(n.left)
        
        if n.right is not None:
            q.append(n.right)
    
    return levels

if __name__ == "__main__":
    node = TreeNode(0, TreeNode(1), TreeNode(2))
    print(levelOrder(node))

            
