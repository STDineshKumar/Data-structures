import unittest

class test_DifferentialLinkedList(unittest.TestCase):

    def setUp(self):
        from ..DifferentialDoubleLinkedList.Differential_linked_list import DifferentialLinkedList
        self.linked_list = DifferentialLinkedList(1)
        self.linked_list.add_node(2)

    def test_Differential_linked_list_head(self):
        from ..DifferentialDoubleLinkedList.Differential_list_element import DifferentialListElement
        self.assertIsInstance(self.linked_list.head,DifferentialListElement)
        self.assertEqual(self.linked_list.head.data_IO,1)
        self.assertIsNotNone(self.linked_list.head.diff_reference)

    def test_gets(self):
        self.assertIsNone(self.linked_list.get_prev(self.linked_list.head))
        self.assertIsNotNone(self.linked_list.get_next(self.linked_list.head))

    def test_length(self):
        self.assertEqual(len(self.linked_list),2)
