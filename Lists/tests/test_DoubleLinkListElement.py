# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 21:57:52 2017

@author: Sagar
"""
import unittest

class test_DoubleLinkListElement(unittest.TestCase):
    def setUp(self):
        from ..DoubleLinkedList.DoubleLinkedList import DoubleLinkListElement
        self.llist = DoubleLinkListElement()
        
    def test_set_data(self):
        self.llist.set_data(43)
        self.assertNotEqual(self.llist.get_data(),None)
    
    def test_set_next(self):
        from ..DoubleLinkedList.DoubleLinkedList import DoubleLinkListElement
        self.llist.set_next(DoubleLinkListElement())
        self.assertIsNotNone(self.llist.get_next())
    
    def test_set_prev(self):
        from ..DoubleLinkedList.DoubleLinkedList import DoubleLinkListElement
        self.llist.set_prev(DoubleLinkListElement())
        self.assertIsNotNone(self.llist.get_prev())
        
    def test_get_data(self):
        self.llist.set_data(43)
        self.assertEqual(self.llist.get_data(),43)
        
    def test_is_head(self):
        self.assertTrue(self.llist.is_head())
    
    def test_is_tail(self):
        self.assertTrue(self.llist.is_tail())
        
    def test_has_prev_element(self):
        self.assertIsNone(self.llist.has_prev())
    
    def test_has_next_element(self):
        self.assertIsNone(self.llist.has_next())