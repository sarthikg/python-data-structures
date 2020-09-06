class Node():
  def __init__(self, value):
    self.value = value
    self.next = None

class SinglyLinkedList():
  def __init__(self):
    self.length = 0
    self.head = None
    self.tail = None

  def __repr__(self):
    if self.length > 0:
      currentNode = self.head
      outputString = ''
      for i in range(0, self.length):
        outputString += str(currentNode.value) + ' --> '
        currentNode = currentNode.next
      return str(self.head.value) + ' | ' + str(self.tail.value) + ' | ' + str(self.length) + ' | ' + outputString
    else:
      return '## | ## | 0 | '

  def push(self, value):
    newNode = Node(value)
    if self.length == 0:
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.next = newNode
      self.tail = newNode
    self.length += 1

  def pop(self):
    returnValue = self.tail.value
    if self.length == 1:
      self.head = None
      self.tail = None
    elif self.length > 1:
      currentNode = self.head
      for i in range(0, self.length-2):
        currentNode = currentNode.next
      self.tail = currentNode
      self.tail.next = None
    else:
      return None
    self.length -= 1
    return returnValue

  def shift(self):
    if self.length != 0:
      self.head = self.head.next
      self.length -= 1

  def unshift(self, value):
    newNode = Node(value)
    if self.length == 0:
      self.tail = newNode
    else:
      newNode.next = self.head
    self.head = newNode
    self.length += 1

  def get(self, position):
    if position < self.length and position >=0:
      currentNode = self.head
      for i in range(0, position):
        currentNode = currentNode.next
      return currentNode.value
    else:
      return None

  def set(self, position, value):
    if position < self.length and position >= 0:
      currentNode = self.head
      for i in range(0, position):
        currentNode = currentNode.next
      currentNode.value = value

  def insert(self, position, value):
    if position == 0:
      self.unshift(value)
    elif position == self.length-1:
      self.push(value)
    elif position < self.length-1 and position > 0:
      currentNode = self.head
      for i in range(0, position-1):
        currentNode = currentNode.next
      newNode = Node(value)
      newNode.next = currentNode.next
      currentNode.next = newNode
      self.length +=1

  def remove(self, position):
    if position == 0:
      self.shift()
    elif position == self.length - 1:
      self.pop()
    elif position > 0 and position < self.length-1:
      currentNode = self.head
      for i in range(0, position-1):
        currentNode = currentNode.next
      currentNode.next = currentNode.next.next
      self.length -=1

  def reverse(self):
    temp = self.head
    self.head = self.tail
    self.tail = temp
    prevNode = self.tail
    currentNode = prevNode.next
    nextNode = None
    for i in range(0, self.length-2):
      nextNode = currentNode.next
      print(prevNode.value, currentNode.value, nextNode.value)
      currentNode.next = prevNode
      prevNode = currentNode
      currentNode = nextNode
    currentNode.next = prevNode