def findAround(matriz, position):
  waterAreas = 1

  try: # Right
    if matriz[position[0]][position[1] + 1] < 0:
      
      matriz[position[0]][position[1] + 1] = 0

      right = findAround(matriz, [ position[0], position[1] + 1 ])

      waterAreas += right
      
  except IndexError:
    pass
  except Exception as e: print(e)

  try:  # Down 
    if matriz[position[0] + 1][position[1]] < 0:

      matriz[position[0] + 1][position[1]] = 0

      down = findAround(matriz, [ position[0] + 1, position[1]])

      waterAreas += down

  except IndexError:
    pass
  except Exception as e: print(e)

  try: # Left
    if matriz[position[0]][position[1] - 1] < 0:
      
      matriz[position[0]][position[1] - 1] = 0

      left = findAround(matriz, [ position[0], position[1] - 1 ])
  
      waterAreas += left
  except IndexError:
    pass
  except Exception as e: print(e)
  
  try: # Up
    if matriz[position[0] - 1][position[1]] < 0:
      
      matriz[position[0] - 1][position[1]] = 0
      up = findAround(matriz, [position[0] - 1, position[1]])
      waterAreas += up
  except IndexError:
    pass
  except Exception as e: print(e)

  return waterAreas
