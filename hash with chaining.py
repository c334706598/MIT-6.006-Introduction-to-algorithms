# -*- coding: utf-8 -*-
"""
Created on Tue May 22 20:18:08 2018

@author: XIN
"""

class hashTable(object):
    def __init__(self, size = 16):
        self.size = size
        self.datasize = 0
        self.data = [LinkedList(None) for _ in range(self.size)]
    
    def find(self, key):
        return self._find(self.Hash(key), key)
        
    def _find(self, index, key):
        current_node = self.data[index]
        if current_node.value == key:
            return current_node
        else:
            while current_node.next != None:
                current_node = current_node.next
                if current_node.value == key:
                    return current_node
            return None
        
    def delete(self, key):
        node_found = self.find(key)
        if node_found:
            if node_found.prev == None:
                node_found.value = None
            else:
                node_found.prev.next = node_found.next
            self.datasize -= 1
        if self.datasize <= self.size // 4 and self.size >= 16:
            self.shrinkTable()
            
    def insert(self, key):
        if self.find(key):
            pass
        else:
            self._insert(self.Hash(key), key)
        if self.datasize >= self.size:
            self.growTable()
                
    def _insert(self, index, key):
        if self.data[index].value == None:
            self.data[index].value = key
        else:
            new_node = LinkedList(key)
            current_node = self.data[index]
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
        self.datasize += 1        

    def find_all_keys(self):
        keys = []
        for slot in self.data:
            current_node = slot
            if current_node.value == None:
                continue
            else:
                keys.append(current_node.value)
                while current_node.next != None:
                    current_node = current_node.next
                    keys.append(current_node.value)
        return keys
                    
    def growTable(self):
        all_keys = self.find_all_keys()
        self.size *= 2
        self.datasize = 0
        self.data = [LinkedList(None) for _ in range(self.size)]
        for key in all_keys:
            self._insert(self.Hash(key), key)
            
    
    def shrinkTable(self):
        all_keys = self.find_all_keys()
        self.size //= 2
        self.datasize = 0
        self.data = [LinkedList(None) for _ in range(self.size)]
        for key in all_keys:
            self._insert(self.Hash(key), key)
    
    def Hash(self, key):
        return key % self.size
    
    def print_out(self):
        for slot in self.data:
            current_node = slot
            temp = []
            if current_node.value == None:
                print('X')
            else:
                temp.append(str(current_node.value))
                while current_node.next != None:
                    current_node = current_node.next
                    temp.append(str(current_node.value))
                temp.append('X')
                print('-->'.join(temp))
                    
class LinkedList(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
        
if __name__ == '__main__':
    h1 = hashTable()
    a = [1,13,44]
    print(a)
    for element in a:
        h1.insert(element)
    h1.insert(23)
    h1.insert(24)
    h1.insert(23)
    h1.delete(3)
    h1.delete(23)
    print(h1.datasize, h1.size)
    h1.print_out()
            
    