# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 19:02:28 2017

@author: Sagar
"""

class DifferentialListElement(object):
    """
    Differential addressed double linked list basic element structure
    abstract data type.Which consists of Data and Differential address component
    generally XOR operation done by previous and next address.
    """
    def __init__(self):
        self.__data = None
        self.__differential_addr = None

    @property
    def data_IO(self):
        return self.__data

    @data_IO.setter
    def data_IO(self,data):
        self.__data = data

    @property
    def diff_reference(self):
        return self.__differential_addr

    @diff_reference.setter
    def diff_reference(self,val):
        prev = None
        nxt = None
        if(len(val) == 1 and type(val) is tuple):
            nxt = val[0]
            self.__differential_addr = id(nxt) ^ 0
        elif(len(val) == 2 and type(val) is tuple):
            prev,nxt = val
            self.__differential_addr = id(prev) ^ id(nxt)
        else:
            print("Invalid number of arguments please give 1 or 2 arguments")

    @classmethod
    def create_node(cls,data):
        "object factory method for generate one elementary node."
        element = DifferentialListElement()
        element.data_IO = data
        return element
