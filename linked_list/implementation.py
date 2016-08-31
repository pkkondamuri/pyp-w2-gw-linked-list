from .interface import AbstractLinkedList
from .node import *

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None
    
        if elements:
            for elem in elements:
                self.append(elem)
        
        
    def __str__(self):
        list_str = []
        self_start = self.start
        while self_start:
            list_str += [self_start.elem]
            self_start = self_start.next
        return str(list_str)

    def __len__(self):
        length = 0
        for elem in self:
            length +=1
        return length

    def __iter__(self):
        n = self.start
        while n:
            yield n
            n = n.next

    def __getitem__(self, index):
        item = self.start
        for ind in range(index):
            item = item.next
        return item
            
            

    def __add__(self, other):
        new_list = LinkedList()
        for elem1 in self:
            new_list.append(elem1.elem)
        for elem2 in other:
            new_list.append(elem2.elem)
        return new_list

    def __iadd__(self, other):
        for elem2 in other:
            self.append(elem2.elem)
        return self

    def __eq__(self, other):
        
        if len(self) != len(other):
            return False
        for elem1 in zip(self,other):
            if elem1[0].elem != elem1[1].elem:
                return False
        return True
    def __ne__(self, other):
        return not self.__eq__(other)
        
    def append(self, elem):
        if self.start is None:        #when append is called in _init_, check to see if self.start is None
            self.start = Node(elem)   #if it is, change the self.start to the first element in the list
            self.end = self.start     #also set the self.end to that element
            return
            
        next_node = Node(elem)
        self.end.next = next_node
        self.end = next_node

    def count(self):
        
        return self.__len__()

    def pop(self, index=None):
        if index == None:
            index = len(self)-1
        if not self.start or index >= len(self) or index < 0:
            raise IndexError
        if index == 0:
            pop_elem = self.start.elem
            self.start = self.start.next
            return pop_elem
        elif index == len(self)-1:
            prev_item = self.__getitem__(index-1)
            item = self.__getitem__(index)
            pop_elem = item.elem
            prev_item.next = None
            return pop_elem
        else:
            prev_item = self.__getitem__(index-1)
            item = self.__getitem__(index)
            pop_elem = item.elem
            prev_item.next = item.next
            return pop_elem
            
        
    
    
