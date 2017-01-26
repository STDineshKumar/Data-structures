# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 23:18:14 2017

@author: Sagar
"""
from .tree_node import Tree_node

class Binary_search_tree(object):
    def __init__(self,*args):
        self.__trunk = Tree_node()
        
    @classmethod
    def add_node(cls,trunk,data):
        node = Tree_node()
        node.data = data
        if trunk.left_subtree is None and trunk.right_subtree is None:
        
    def __str__(self):
        pass
    
    def __repr__(self):
        pass
    
    @classmethod
    def is_head(cls):
        pass
        