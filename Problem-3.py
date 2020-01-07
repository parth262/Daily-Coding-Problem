'''
From: Google
Difficulty: Medium

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

'''

import re

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "%s<%s,%s>" % (str(self.val), str(self.left), str(self.right))


node = Node('root', Node('left', Node('left.left')), Node('right'))

def serialize(tree):
    return str(tree)

node_serialized = serialize(node)
print(node_serialized)