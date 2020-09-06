class Node():
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack():
  def __init__(self):
    self.first = None
    self.last = None
    self.size = 0

  def __repr__(self):
    if self.size > 0:
      currentNode = self.first
      outputString = ''
      for i in range(0, self.size):
        outputString += str(currentNode.value) + ' --> '
        currentNode = currentNode.next
      return str(self.first.value) + ' | ' + str(self.last.value) + ' | ' + str(self.size) + ' | ' + outputString
    else:
      return '## | ## | 0 | '

  def push(self, value):
    newNode = Node(value)
    if self.size == 0:
      self.first = newNode
      self.last = newNode
    else:
      newNode.next = self.first
      self.first = newNode
    self.size += 1

  def pop(self):
    if self.size == 0:
      return None
    returnValue = self.first.value
    if self.size == 1:
      self.first = None
      self.last = None
    else:
      currentNode = self.first.next
      self.first.next = None
      self.first = currentNode
    self.size -= 1
    return returnValue