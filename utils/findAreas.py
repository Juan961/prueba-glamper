from .searchAround import findAround

def findAreas(matriz):
  areas = []

  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      if matriz[i][j] < 0:
        matriz[i][j] = 0
        findedAreas = findAround(matriz, [i, j])
        areas.append(findedAreas)
        
  return areas
