class Node():
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

class DoublyLinkedList():
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def __repr__(self):
    if self.length > 0:
      currentNode = self.head
      outputString = '<-> '
      for i in range(0, self.length):
        outputString += str(currentNode.value) + ' <-> '
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
      newNode.prev = self.tail
      self.tail = self.tail.next
    self.length +=1

  def pop(self):
    if self.length == 1:
      returnValue = self.head.value
      self.head = None
      self.tail = None
    elif self.length > 1:
      returnValue = self.tail.value
      lastNode = self.tail
      self.tail = self.tail.prev
      lastNode.prev = None
      self.tail.next = None
    else:
      return None
    self.length -= 1
    return returnValue

  def shift(self):
    firstNode = self.head
    if self.length == 1:
      self.head = None
      self.tail = None
    elif self.length > 1:
      self.head = self.head.next
      self.head.prev = None
      firstNode.next = None
    self.length -= 1
    return firstNode.value

  def unshift(self, value):
    newNode = Node(value)
    if self.length == 0:
      self.head = newNode
      self.tail = newNode
    newNode.next = self.head
    self.head.prev = newNode
    self.head = newNode
    self.length += 1

  def get(self, position):
    if position >=0 and position < self.length:
      midpoint = self.length // 2
      if position < midpoint:
        startPoint = self.head
        for i in range(0, position):
          startPoint = startPoint.next
      else:
        startPoint = self.tail
        for i in range(0, self.length - position -1):
          startPoint = startPoint.prev
      return startPoint.value
    else:
      return None

  def set(self, position, value):
    if position >=0 and position < self.length:
      midpoint = self.length // 2
      if position < midpoint:
        startPoint = self.head
        for i in range(0, position):
          startPoint = startPoint.next
      else:
        startPoint = self.tail
        for i in range(0, self.length - position -1):
          startPoint = startPoint.prev
      startPoint.value = value

  def insert(self, position, value):
    if position == 0:
      self.unshift(value)
    elif position == self.length:
      self.push(value)
    elif position > 0 and position < self.length:
      newNode = Node(value)
      midpoint = self.length // 2
      if position < midpoint:
        startPoint = self.head
        for i in range(0, position):
          startPoint = startPoint.next
      else:
        startPoint = self.tail
        for i in range(0, self.length - position -1):
          startPoint = startPoint.prev
      prevNode = startPoint.prev
      prevNode.next = newNode
      newNode.prev = prevNode
      newNode.next = startPoint
      startPoint.prev = newNode
      self.length += 1

  def remove(self, position):
    if position == 0:
      self.shift()
    elif position == self.length-1:
      self.pop()
    elif position > 0 and position < self.length-1:
      midpoint = self.length // 2
      if position < midpoint:
        startPoint = self.head
        for i in range(0, position):
          startPoint = startPoint.next
      else:
        startPoint = self.tail
        for i in range(0, self.length - position -1):
          startPoint = startPoint.prev
      prevNode = startPoint.prev
      nextNode = startPoint.next
      nextNode.prev = prevNode
      prevNode.next = nextNode
      startPoint.next = None
      startPoint.prev = None
      self.length -= 1