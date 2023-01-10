class BinaryTreeNode:
  def __init__(self, value : int) -> None:
    self.__value__ = value
    self.__left__ = None
    self.__right__ = None
  def setLeft(self, left) -> None:
    self.__left__ = left
  def setRight(self, right) -> None:
    self.__right__ = right
  def getValue(self) -> int:
    return self.__value__
  def getLeft(self):
    return self.__left__
  def getRight(self):
    return self.__right__
  def __repr__(self) -> str:
    return str(self.getValue())
  def __str__(self) -> str:
    return str(self.getValue())

class BinaryTree:
  def __init__(self, root : BinaryTreeNode) -> None:
    self.__root__ = root
  def getRoot(self) -> BinaryTreeNode:
    return self.__root__
  def preorder(self, start : BinaryTreeNode) -> list[BinaryTreeNode]:
    result = [start]
    if start.getLeft() != None:
      result.extend(self.preorder(start.getLeft()))
    if start.getRight() != None:
      result.extend(self.preorder(start.getRight()))
    return result
  def inversePreorder(self, start : BinaryTreeNode) -> list[BinaryTreeNode]:
    result = [start]
    if start.getRight() != None:
      result.extend(self.inversePreorder(start.getRight()))
    if start.getLeft() != None:
      result.extend(self.inversePreorder(start.getLeft()))
    return result