import unittest

class test_DifferentialLinkedList(unittest.TestCase):

    def setUp(self):
        from ..DifferentialDoubleLinkedList.Differential_linked_list import DifferentialLinkedList
        self.linked_list = DifferentialLinkedList(1)
