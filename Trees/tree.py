import abc
class Tree:
    __metaclass__ = abc.ABCMeta

    @abstractmethod
    def add_node(self,tree,data):
       raise NotImplementedError("Mandatory to implement for node addition to tree")

    @abstractmethod
    def inorder(self,tree):
       raise NotImplementedError("inorder traversal data in the tree make it a generator")

    @abstractmethod
    def posorder(self,tree):
      raise NotImplementedError("postorder traversal data in the tree make it a generator")

    @abstractmethod
    def preorder(self,tree):
      raise NotImplementedError("preorder traversal data in the tree make it a generator")

    @abstractmethod
    def search(self,data):
       raise NotImplementedError("Implement this for searching data in the tree")

    @abstractmethod
    def remove(self,data):
        raise NotImplementedError("Implement this to search and remove a data from the tree")
