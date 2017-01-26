# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 20:40:59 2017

@author: Sagar
"""
import unittest

class test_DifferentialListElement(unittest.TestCase):
    """
    TestCase for testing all the basic funcationalities of 
    DifferentialListElement class
    """

    def setUp(self):
        from ..DifferentialDoubleLinkedList.Differential_list_element import DifferentialListElement
        self.element_obj = DifferentialListElement()
        
    def test_data_IO(self):
        self.assertIsNone(self.element_obj.data_IO,"Problem with property data_IO")
        self.element_obj.data_IO = 43
        self.assertIsNotNone(self.element_obj.data_IO,"Problem with property data_IO")
    
    def test_diff_reference(self):
        self.assertEqual(int(self.element_obj.diff_reference),0)
        self.element_obj.diff_reference = [10]
        self.assertEqual(self.element_obj.diff_reference,id(10) ^ id(None))
        self.element_obj.diff_reference = [10,20]
        self.assertEqual(self.element_obj.diff_reference,id(10) ^ id(20))
        self.element_obj.diff_reference = [10,20,30]
        
    def test_create_node(self):
        self.assertIsInstance(self.element_obj.create_node(2),self.element_obj.__class__)