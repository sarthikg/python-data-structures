class Node():
  def __init__(self, value):
    self.value = value
    self.next = None

class Queue():
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
  
  def enqueue(self, value):
    newNode = Node(value)
    if self.size == 0:
      self.first = newNode
      self.last = newNode
    else:
      self.last.next = newNode
      self.last = newNode
    self.size += 1
  
  def dequeue(self):
    if self.size == 0:
      return None
    elif self.size == 1:
      currentNode = self.first
      currentNode.next = None
      self.first = None
      self.last = None
    else:
      currentNode = self.first
      self.first = currentNode.next
      currentNode.next = None
    self.size -= 1
    return currentNode.value  