class LinkedListNode:
  def __init__(self, value : int) -> None:
    self.__value__ = value
    self.__next__ = None
  def setNext(self, next) -> None:
    self.__next__ = next
  def getValue(self) -> int:
    return self.__value__
  def getNext(self):
    return self.__next__
  def __str__(self) -> str:
    s = f'[{self.getValue()}]'
    if self.getNext() != None: s += ' -> '
    return s

def getLinkedList(first : LinkedListNode) -> str:
  s = ''
  node = first
  while True:
    s += str(node)
    node = node.getNext()
    if (node == None):
      break
  return s


def invertList(first : LinkedListNode) -> LinkedListNode:
  saveList : list[int] = []
  node = first
  # Save all values
  while True:
    saveList.append(node.getValue())
    node = node.getNext()
    if (node == None):
      break
  # Make new list in inverted order
  firstNode = LinkedListNode(saveList.pop())
  oldNode = firstNode
  while len(saveList) > 0:
    newNode = LinkedListNode(saveList.pop())
    oldNode.setNext(newNode)
    oldNode = newNode
  return firstNode