from linkedList import LinkedListNode

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