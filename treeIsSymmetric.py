from binaryTree import BinaryTreeNode, BinaryTree

def isSymmetric(root : BinaryTreeNode) -> bool:
  if (root.getLeft() == None and root.getRight() == None):
    return True
  elif (root.getLeft() == None or root.getRight() == None):
    return False
  leftTree = BinaryTree(root.getLeft())
  rightTree = BinaryTree(root.getRight())
  leftContent = leftTree.preorder(leftTree.getRoot())
  rightContent = rightTree.inversePreorder(rightTree.getRoot())
  if len(leftContent) != len(rightContent):
    return False
  
  while len(leftContent) > 0:
    if leftContent.pop().getValue() !=  rightContent.pop().getValue():
      return False
  return True