# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 23:32:06 2017

@author: Sagar
"""
class Tree_node(object):
    def __init__(self):
        self.__data = None
        self.__left = None
        self.__right = None
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self,info):
        self.__data = info
    
    @property
    def left_subtree(self):
        return self.__left
    
    @left_subtree.setter
    def left_subtree(self, tree):
        self.__left = tree
        
    @property
    def right_subtree(self):
        return self.__right
        
    @right_subtree.setter
    def right_subtree(self, tree):
        self.__right = tree        