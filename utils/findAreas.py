from .searchAround import findAround

def findAreas(matrix):
  areas = []

  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] < 0:
        matrix[i][j] = 0
        findedAreas = findAround(matrix, [i, j])
        areas.append(findedAreas)
        
  return areas
