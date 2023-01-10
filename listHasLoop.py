from linkedList import LinkedListNode

def hasLoop(first : LinkedListNode) -> bool:
  ids : list[int] = []
  node = first
  while True:
    i = id(node)
    if ids.count(i) > 0: return True
    ids.append(i)
    node = node.getNext()
    if (node == None):
      break
  return False