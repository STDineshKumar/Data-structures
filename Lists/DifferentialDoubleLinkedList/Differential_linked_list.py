# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:22:26 2017

@author: Sagar
"""

from gc import gc_objects
from . import DifferentialListElement

class DifferentialLinkedList(DifferentialListElement):

    def __init__(self, data):
        self.head = super().create_node(data)
        self.head.diff_reference = (0,)
        self.prev_addr = 0
        self.current = self.head

    def add_node(self, data):
        if self.head.diff_reference == 0:
            self.head.diff_reference = (id(super().create_node(data)),)
        else:
            next_obj = DifferentialLinkedList.get_next(self.current)
            self.prev_addr = id(self.current)
            self.current = next_obj
            self.current.add_node(data)

    @classmethod
    def get_next(cls, node):
        id_code = node.diff_reference ^ self.prev_addr
        for obj in gc_objects():
            if id(obj) == id_code:
                return obj
        return None

    @classmethod
    def get_prev(cls, node):
        for obj in gc_objects():
            if id(obj) == self.prev_addr:
                return obj
        return None

    @classmethod
    def has_prev(cls, node):
        pass

    @classmethod
    def has_next(cls, node):
        pass

    def remove(self, data):
        pass

    def insert(self, index, data):
        pass

    def remove_idx(self, idx):
        pass

    def __len__(self):
        count = 1
        self.current = self.head
        while(self.current):
            count += 1
            self.current = self.get_next(self.current)
        return count
