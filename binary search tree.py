# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 21:07:38 2017

@author: XIN
"""

class BinarySearchTree:
    def __init__(self):    # initialize a empty Binary Search Tree
        self.root = None
        self.size = 0
        
    def length(self):     # get the size of the Binary Search Tree   
        return self.size
    
    def __len__(self):    # get the size of the Binary Search Tree
        return self.size
    
    def __iter__(self):   # iterator
        return self.root.__iter__()
    
    def put(self, key, val): # put an element into Binary Search Tree
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1
        
    def _put(self, key, val, current_node): # put helper
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent = current_node)
        elif key > current_node.key:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent = current_node)
        else:
            current_node.payload = val
            
    def __setitem__(self, k ,v):
        self.put(k, v)
        
    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
        
    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)
        
    def __getitem__(self, key):
        return self.get(key)
    
    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False
        
    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')
            
    def remove(self, current_node):
        if current_node.has_both_children(): # if current_node has both children, find the successor and replace the current_node
            temp_node = self._successor(current_node) # find the successor
            
            self.remove(temp_node)         # remove the successor from the tree
                        
            temp_node.parent = current_node.parent   # bidirectional link the successor to the new parent
            
            if current_node.is_left_child():
                temp_node.parent.left_child = temp_node
            if current_node.is_right_child():
                temp_node.parent.right_child = temp_node
                
            if current_node.has_left_child():    # bidirectional link the successor to new children
                temp_node.left_child = current_node.left_child
                temp_node.left_child.parent = temp_node
                
            if current_node.has_right_child():
                temp_node.right_child = current_node.right_child
                temp_node.right_child.parent = temp_node

        elif current_node.has_left_child():    # if current_node only has left chidren, replace the current_node with its left children
            temp_node = current_node.left_child
            
            temp_node.parent = current_node.parent # bidirectional link the temp_node to the new parent
            if current_node.is_left_child():
                temp_node.parent.left_child = temp_node
            if current_node.is_right_child():
                temp_node.parent.right_child = temp_node
                
        elif current_node.has_right_child():    # if current_node only has right children, replace the current
            temp_node = current_node.right_child
            
            temp_node.parent = current_node.parent # bidirectional link the temp_node to the new parent
            if current_node.is_left_child():
                temp_node.parent.left_child = temp_node
            if current_node.is_right_child():
                temp_node.parent.right_child = temp_node
        
        else:                                   # the current_node is a leaf
            if current_node.is_left_child():
                temp_node.parent.left_child = None
            if current_node.is_right_child():
                temp_node.parent.right_child = None
                        
    def __delitem__(self, key):
        self.delete(key)
        
    def findmin(self):
        if self.size > 0:
            return self._findmin(self.root)
        else:
            return None
    
    def _findmin(self, current_node):
        while current_node.has_left_child():
            current_node = current_node.left_child
        return current_node
    
    def findmax(self):
        if self.size > 0:
            return self._findmax(self.root)
        else:
            return None
        
    def _findmax(self, current_node):
        while current_node.has_right_child():
            current_node = current_node.right_child
        return current_node
    
    def successor(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return self._successor(res)
            else:
                return None
        else:
            return None
    
    def _successor(self, current_node):
        if current_node.has_right_child():        # If current_node has right child, find the smallest in the right child
            current_node = current_node.right_child
            while current_node.has_left_child():
                current_node = current_node.left_child
            return current_node
        elif current_node.is_left_child():       # else if the node is left child, its parent is the successor
            return current_node.parent
        elif current_node.is_right_child():      # else if the current node is a right child, go all the way to the left_up direction, then find the parent
            while current_node.is_right_child():
                current_node = current_node.parent
            return current_node.parent
        else:                                    # current_node is the root and has no right child
            return None
            
    def predecessor(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return self._predecessor(res)
            else:
                return None
        else:
            return None

    def _predecessor(self, current_node):              
        if current_node.has_left_child():           # If current_node has left child, the predecessor is the largest node in the left child
            current_node = current_node.left_child
            while current_node.has_right_child():
                current_node = current_node.right_child
            return current_node
        elif current_node.is_right_child():        # else if the current_node is a right child, its parent the predecessor
            return current_node.parent
        elif current_node.is_left_child():         # else if the current_node is a left child, go all the way to the right_up direction, then find the parent of taht node
            while current_node.is_left_child():
                current_node = current_node.parent
            return current_node.parent
        else:                                      # current_node is the roor and has no left child
            return None
    
    def inorder(self):
        current_node = self.root
        self._inorder(current_node)

    def preorder(self):
        current_node = self.root
        self._preorder(current_node)

    def postorder(self):
        current_node = self.root
        self._postorder(current_node)
        
    def _inorder(self, current_node):
        if current_node.has_left_child():
            self._inorder(current_node.left_child)
        print("{",current_node.key,":",current_node.payload,"}\n")
        if current_node.has_right_child():
            self._inorder(current_node.right_child)

    def _preorder(self, current_node):
        print("{",current_node.key,":",current_node.payload,"}\n")
        if current_node.has_left_child():
            self._preorder(current_node.left_child)
        if current_node.has_right_child():
            self._preorder(current_node.right_child)
        
    def _postorder(self, current_node):
        if current_node.has_left_child():
            self._postorder(current_node.left_child)
        if current_node.has_right_child():
            self._postorder(current_node.right_child)
        print("{",current_node.key,":",current_node.payload,"}\n")        
        
class TreeNode:
    def __init__(self, key, val, left = None, right = None, parent = None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent
        
    def has_left_child(self):
        return self.left_child
    
    def has_right_child(self):
        return self.right_child
    
    def is_left_child(self):
        return self.parent and self.parent.left_child == self
    
    def is_right_child(self):
        return self.parent and self.parent.right_child == self
    
    def is_root(self):
        return not self.parent
    
    def is_leaf(self):
        return not (self.left_child or self.right_child)
    
    def has_any_children(self):
        return self.left_child or self.right_child
    
    def has_both_children(self):
        return self.left_child and self.right_child
    
    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self
        
#import random
#        
#a = BinarySearchTree()
#b = [int(random.uniform(0,100)) for _ in range(20)]
#print(b)
#
#for x in b:
#    a.put(x, x)

#a.inorder()
#a.postorder()         
#a.preorder()
#print(a.findmax().payload)
#print(a.findmin().payload)
#MIN = a.findmin()
#current_node = MIN
#while a.successor(current_node.key):
#    print(current_node.payload)
#    current_node = a.successor(current_node.key) 
#MAX = a.findmax()
#current_node = MAX
#while a.predecessor(current_node.key):
#    print(current_node.payload)
#    current_node = a.predecessor(current_node.key) 
    