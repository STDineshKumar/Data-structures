# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 20:28:40 2017

@author: Sagar

@Description: Classical double linked list with 2 address next and previous and 
              one data attribute.

"""
class DoubleLinkListElement(object):
     ''' Class to generate and granular element for Doublelinked list
         with basic validation for further processing
     '''
     
     def __init__(self):
        ''' Uninit basic attributes fo doublelinklist
        '''
        self.__data = None
        self.__next = None
        self.__prev = None

     def get_data(self):
        '''Fetches data from element structure
        '''
        return self.__data
     
     def get_prev(self):
        '''Fetches previous attribute from element structure
        '''
        return self.__prev

     def get_next(self):
        '''Fetches next attribute from element structure
        '''
        return self.__next

     def set_data(self, data):
        '''Puts data into element structure
        '''
        self.__data = data

     def set_next(self, nxt):
        '''Puts next element structure into next attribute
        '''
        self.__next = nxt

     def set_prev(self, prev):
        '''Puts previous element structure into prev attribute
        '''
        self.__prev = prev

     def has_next(self):
         '''Checks the existance of next attribute
        '''
         return self.__next if self.__next is not None else None

     def has_prev(self):
         '''Checks the existance of prev attribute
         '''
         return self.__prev if self.__prev is not None else None

     def is_head(self):
         '''Checks the current element is head
         '''
         return True if self.__prev is None else False

     def is_tail(self):
         '''Checks the current element is tail
         '''
         return True if self.__next is None else False

class DoubleLinkList(DoubleLinkListElement):
     
  @classmethod
  def create_node(cls, data):
     element = DoubleLinkListElement()
     element.set_data(data)
     return element
     
  def __init__(self, data):
       self.head = DoubleLinkList.create_node(data)
       self.current = self.head
  
  def append_node(self, data):
      current = self.head
      while current.has_next():
          current = current.get_next()
      else:
         current.set_next(DoubleLinkList.create_node(data))
         current.get_next().set_prev(current)
 
  def __len__(self):
      count = 1
      current = self.head
      while current.has_next():
          count += 1
          current = current.get_next()
      return count
      
  def pop(self):
      while self.current.has_next():
          self.current = self.current.get_next()
      else:
          data = self.current.get_data()
          self.current = self.current.get_prev()
          self.current.set_next(None)
          return data
         
  def __iter__(self):
      current = self.head
      while(current.has_next()):
            yield current
            current = current.get_next()
      yield current
            
  def insert(self,idx,data):
      if 0 <= idx < len(self):
          for indx,element in enumerate(iter(self)):
              if idx == indx and idx != 0:
                  new_node = DoubleLinkList.create_node(data)
                  new_node.set_next(element)
                  new_node.set_prev(element.get_prev())
                  element.set_prev(new_node)
                  new_node.get_prev().set_next(new_node)
                  break
              elif idx ==indx and idx == 0:
                  self.head.set_prev(DoubleLinkList.create_node(data))
                  self.head.get_prev().set_next(self.head)
                  self.head=self.head.get_prev()
                  self.head.set_prev(None)
                  break
  @staticmethod
  def remove(linkedlist,data):
      current = linkedlist.head
      
      while current.get_data() != data and current.has_next():
          current = current.get_next()
          
      if current.get_data() == data and current.is_head():
          current = linkedlist.head.get_next()
          linkedlist.head.set_next(None)
          linkedlist.head = current
          linkedlist.head.set_prev(None)
          return data        
          
      elif current.get_data() == data and current.is_tail():
          current.get_prev().set_next(None)
          current.set_prev(None)
          current = None
          return data
          
      elif current.get_data() == data:
          current.get_prev().set_next(current.get_next())
          current.get_next().set_prev(current.get_prev())
          current.set_prev(None)
          current.set_next(None)
          current = None
          return data
      else:
          return("Data not in the Double linked list")
  
  def remove_idx(self,idx):
      current = self.head
      for indx in range(len(self)):
          if idx == 0 and current.is_head():
              self.head = current.get_next()
              self.head.set_prev(None)
              current.set_next(None)
              break
          
          elif idx == indx and current.is_tail():
              current.get_prev().set_next(None)
              current.set_prev(None)
              break
              
          elif indx == idx and not current.is_head() and not current.is_tail():
              current.get_prev().set_next(current.get_next())
              current.get_next().set_prev(current.get_prev())
              current.set_next(None)
              current.set_prev(None)
              current = None
              break
          else:
              current = current.get_next()
              
          
          
  def __repr__(self):
      current = self.head
      data = []
      while current.has_next():
          data.append(current.get_data())
          current = current.get_next()
      else:
          data.append(current.get_data())
          return "Linked list contains::{0}\n".format(data)
  
  def __str__(self):
      return self.__repr__()
