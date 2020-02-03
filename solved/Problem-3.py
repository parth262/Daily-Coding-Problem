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
        return "Node(%s, %s, %s)" % (self.val, self.left, self.right)


node = Node('root', Node('left', Node('left.left')), Node('right'))

def serialize(tree, index="1"):
    serialized = "%s, %s;" % (tree.val, index)
    if tree.left:
        serialized += serialize(tree.left, index=index + ".1")
    
    if tree.right:
        serialized += serialize(tree.right, index=index + ".2")

    return serialized

def deserialize(tree):
    nodes = tree.split(";")
    node_dict = {}
    for node in nodes[-2::-1]:
        [name, val] = node.split(",")
        node_dict[val.strip()] = Node(name)

    root_node = None

    for key, value in node_dict.items():
        if "." in key:
            last_dot_index = key.rindex(".")
            parent = key[:last_dot_index]
            child = key[last_dot_index+1:]

            parent_node = node_dict[parent]
            if child == '1':
                parent_node.left = value
            else:
                parent_node.right = value
        
        else:
            return value



assert deserialize(serialize(node)).left.left.val == 'left.left'
print("Success")