class Graph():
  def __init__ (self):
    self.aList = {}

  def addVertex(self, vertex):
    self.aList[vertex] = []

  def addEdge(self, vertex1, vertex2):
    self.aList[vertex1].append(vertex2)
    self.aList[vertex2].append(vertex1)

  def removeEdge(self, vertex1, vertex2):
    self.aList[vertex1].remove(vertex2)
    self.aList[vertex2].remove(vertex1)

  def removeVertex(self, vertex):
    removalList = list.copy(self.aList[vertex])
    for v in removalList:
      self.removeEdge(vertex, v)
    self.aList.pop(vertex)
  
  def RecursiveDFS(self, root):
    vertexes = []
    seen = {}
    def helper(vertex):
      vertexes.append(vertex)
      seen[vertex] = True
      for el in self.aList[vertex]:
        if seen.get(el) == None:
          helper(el)
    helper(root)
    return vertexes

  def IterativeDFS(self, root):
    stack = [root]
    vertexes = []
    seen = {root: True}
    while len(stack) != 0:
      vertex = stack.pop()
      vertexes.append(vertex)
      for v in self.aList[vertex]:
        if seen.get(v) == None:
          stack.append(v)
          seen[v] = True
    return vertexes
      
  def IterativeBFS(self, root):
    queue = [root]
    vertexes = []
    seen = {root: True}
    while len(queue) != 0:
      vertex = queue.pop(0)
      vertexes.append(vertex)
      for v in self.aList[vertex]:
        if seen.get(v) == None:
          queue.append(v)
          seen[v] = True
    return vertexes