'''
You are given a binary tree and you need to write a function that can determine if it is height-balanced.

A height-balanced tree can be defined as a binary tree in which the left and right subtrees of every node differ in height by a maximum of 1.

Example 1:
Given the following tree [5,10,25,None,None,12,3]:

    5
   / \
 10  25
    /  \
   12   3
return True.

Example 2:
Given the following tree [5,6,6,7,7,None,None,8,8]:

       5
      / \
     6   6
    / \
   7   7
  / \
 8   8
return False.
'''

'''
CODE :
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

class HeightMeasure:
    def __init__(self):
        self.HeightMeasure = 0
    
def balancedBinaryTree(root, HeightMeasure):
    left_height = HeightMeasure()
    right_height = HeightMeasure()
    
    if root is None:
        return True 
        
    leftnode = balancedBinaryTree(root.left, left_height)
    rightnode = balancedBinaryTree(root, right_height)
    
    HeightMeasure.HeightMeasure = max(left_height.HeightMeasure, right_height.HeightMeasure) + 1
    
    if abs(left_height.HeightMeasure - right_height.HeightMeasure) <=1:
            return leftnode and rightnode
            print(leftnode, rightnode) 
    return False 
    
    if balancedBinaryTree(root, HeightMeasure):
        print('The Binary Tree is balanaced')
    else: 
        print('The Binary Tree is not balanaced')
HeightMeasure = HeightMeasure()
'''


'''
ERR:
Traceback (most recent call last):
  File main.py3 in the pre-written template, in getUserOutputs
    userOutput = _runtgfso(testInputs[i])
  File main.py3 in the pre-written template, in _runtgfso
    return balancedBinaryTree(*_fArgs_nhkzxfgqqffm)
TypeError: balancedBinaryTree() missing 1 required positional argument: 'HeightMeasure'
'''