import math

class WeightedGraph():
  def __init__(self):
    self.aList = {}

  def addVertex(self, vertex):
    self.aList[vertex] = []

  def addEdge(self, vertex1, vertex2, weight):
    self.aList[vertex1].append({'node':vertex2, 'weight':weight})
    self.aList[vertex2].append({'node':vertex1, 'weight':weight})

  def removeEdge(self, vertex1, vertex2):
    for vertex in self.aList[vertex1]:
      if vertex[node] == vertex2:
        self.aList.remove(vertex)
        break
    for vertex in self.aList[vertex2]:
      if vertex[node] == vertex1:
        self.aList.remove(vertex)
        break

  def removeVertex(self, vertex):
    removalList = list.copy(self.aList[vertex])
    for v in removalList:
      self.removeEdge(v, vertex)
    self.aList.pop(vertex)

  def dijkstras(self, start, end):
    shortestDistance = {}
    for vertex in self.aList.keys():
      shortestDistance[vertex] = math.inf
    shortestDistance[start] = 0
    def helper(vertex):
      for subv in self.aList[vertex]:
        if shortestDistance[subv['node']] > (subv['weight'] + shortestDistance[vertex]):
          shortestDistance[subv['node']] = (subv['weight'] + shortestDistance[vertex])
          helper(subv['node'])
    helper(start)
    return shortestDistance[end]