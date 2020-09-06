class HashTable() :
  def __init__(self, length = None):
    self.length = length or 53
    self.keyMap = [None for i in range(0, self.length)]

  def _hash(self, key):
    total = 0
    weirdPrime = 31
    accountedRange = min(len(key), 100)
    for i in range(0, accountedRange):
      total += ord(key[i])
    return (total*weirdPrime) % (self.length)

  def set(self, key, value):
    place = self._hash(key)
    if self.keyMap[place] == None:
      self.keyMap[place] = []
    self.keyMap[place].append([key,value])

  def get(self, key):
    place = self._hash(key)
    if self.keyMap[place] == None:
      return None
    for el in self.keyMap[place]:
      if el[0] == key:
        return el[1]
    return None

  def keys(self):
    keys = []
    for i in range(0, len(self.keyMap)):
      if self.keyMap[i] != None:
        for subel in self.keyMap[i]:
          keys.append(subel[0])
    return keys

  def values(self):
    values = []
    for i in range(0, len(self.keyMap)):
      if self.keyMap[i] != None:
        for subel in self.keyMap[i]:
          values.append(subel[1])
    return values