'''
From: Google
Difficulty: Easy

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
# node = Node(2, Node(2, Node(2), Node(2)), Node(2, Node(2), Node(2)))

def count_univals(tree):
    if tree == None:
        return (0, True)

    left_count, is_left_unival = count_univals(tree.left)
    right_count, is_right_unival = count_univals(tree.right)

    is_unival = True
    if not is_left_unival or not is_right_unival:
        is_unival = False
    
    if tree.left != None and tree.left.val != tree.val:
        is_unival = False
    
    if tree.right != None and tree.right.val != tree.val:
        is_unival = False
    
    if is_unival:
        return (left_count + right_count + 1, True)
    return (left_count + right_count, False)
    
print(count_univals(node))


    

    

