class BinaryHeap():
  def __init__(self):
    self.array = []
  
  def insert(self, value):
    self.array.append(value)
    if len(self.array) > 1:
      current = len(self.array)-1
      parent = (current-1) // 2
      while self.array[parent] < self.array[current] and parent >= 0:
        temp = self.array[parent]
        self.array[parent] = self.array[current]
        self.array[current] = temp
        current = parent
        parent = (current-1) // 2

  def ExtractMax(self):
    if len(self.array) > 0:
      returnValue = self.array[0]
      self.array[0] = self.array[-1]
      self.array.pop()
      def swap(array, pos1, pos2):
        temp = array[pos1]
        array[pos1] = array[pos2]
        array[pos2] = temp
      def helper(position):
        if len(self.array) < (2 * position) + 1:
          return True
        elif len(self.array) > (2 * position) + 1:
          left = (2 * position) + 1
          leftdiff = self.array[left] - self.array[position]
          rightdiff = -1
          if len(self.array) > left + 1:
            right = left + 1
            rightdiff = self.array[right] - self.array[position]
          elif leftdiff > 0:
            swap(self.array, position, left)
            return True
          else:
            return True
          if leftdiff > rightdiff and leftdiff > 0:
            swap(self.array, position, left)
            if len(self.array) == right:
              return True
            else:
              helper(left)
          elif rightdiff > leftdiff and rightdiff > 0:
            swap(self.array, position, right)
            if len(self.array) == right:
              return True
            else:
              helper(right)
      position = 0
      helper(position)
      return returnValue
    else:
      return None