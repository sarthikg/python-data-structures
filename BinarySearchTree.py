class Node():
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  
class BinarySearchTree():
  def __init__(self):
    self.root = None
  
  def insert(self, value):
    newNode = Node(value)
    if self.root == None:
      self.root = newNode
    else:
      currentNode = self.root
      while True:
        if value < currentNode.value:
          if currentNode.left == None:
            currentNode.left = newNode
            break
          else:
            currentNode = currentNode.left
        else:
          if currentNode.right == None:
            currentNode.right = newNode
            break
          else:
            currentNode = currentNode.right
            
  def find(self, value):
    if self.root == None:
      return False
    currentNode = self.root
    while True:
      if value == currentNode.value:
        return True
      elif value < currentNode.value:
        if currentNode.left:
          currentNode = currentNode.left
        else:
          return False
      else:
        if currentNode.right:
          currentNode = currentNode.right
        else:
          return False