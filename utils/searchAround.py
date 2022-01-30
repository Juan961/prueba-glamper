def findAround(matrix, position):
  waterAreas = 1

  try: # Right
    if matrix[position[0]][position[1] + 1] < 0:
      
      matrix[position[0]][position[1] + 1] = 0

      right = findAround(matrix, [ position[0], position[1] + 1 ])

      waterAreas += right
      
  except IndexError:
    pass
  except Exception as e: print(e)

  try:  # Down 
    if matrix[position[0] + 1][position[1]] < 0:

      matrix[position[0] + 1][position[1]] = 0

      down = findAround(matrix, [ position[0] + 1, position[1]])

      waterAreas += down

  except IndexError:
    pass
  except Exception as e: print(e)

  try: # Left
    if matrix[position[0]][position[1] - 1] < 0:
      
      matrix[position[0]][position[1] - 1] = 0

      left = findAround(matrix, [ position[0], position[1] - 1 ])
  
      waterAreas += left
  except IndexError:
    pass
  except Exception as e: print(e)
  
  try: # Up
    if matrix[position[0] - 1][position[1]] < 0:
      
      matrix[position[0] - 1][position[1]] = 0
      up = findAround(matrix, [position[0] - 1, position[1]])
      waterAreas += up
  except IndexError:
    pass
  except Exception as e: print(e)

  return waterAreas
