# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 21:30:59 2017

@author: Sagar
"""
import unittest

class test_DoubleLinkList(unittest.TestCase):
    
    def setUp(self):
        from ..DoubleLinkedList.DoubleLinkedList import DoubleLinkList
        self.llist = DoubleLinkList(1)
        for i in range(2,11):
           self.llist.append_node(i)
        
    def test_length(self):
        self.assertEqual(len(self.llist),10)
        
    def test_pop(self):
        self.llist.pop()
        self.llist.pop()
        self.llist.pop()
        self.assertEqual(len(self.llist),7)
        
    
    #@unittest.skip("codefix needed")
    def test_append_node(self):
        self.llist.append_node(22)
        self.assertEqual(self.llist.pop(),22)
        
    def test_insert(self):
        self.llist.insert(0,43)
        self.assertEqual(self.llist.head.get_data(),43)
        #print(id(self.llist.head.get_next()))
        self.llist.insert(10,45)
        self.llist.pop()
        self.assertEqual(self.llist.pop(),45)
            
    def test_remove(self):
        from ..DoubleLinkedList.DoubleLinkedList import DoubleLinkList
        self.assertEqual(DoubleLinkList.remove(self.llist,4),4)
        self.assertEqual(DoubleLinkList.remove(self.llist,1),1)
        self.assertEqual(DoubleLinkList.remove(self.llist,10),10)
        self.assertEqual(DoubleLinkList.remove(self.llist,20),"Data not in the Double linked list")
        
    #@unittest.skip("codefix needed")
    def test_remove_idx(self):
        self.llist.remove_idx(0)
        self.assertEqual(self.llist.head.get_data(),2)
        self.llist.remove_idx(2)
        self.assertEqual(self.llist.head.get_next().get_next().get_data(),5)
        self.llist.remove_idx(7)
        print(self.llist)
        self.assertNotEqual(self.llist.head.get_next().get_next().get_data(),10)
        
        
    
        
    

        