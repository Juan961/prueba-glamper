import random
from .executionTime import execution_time

def generate(size=1000):
  newMap = [[0 for x in range(size)] for y in range(size)]
  for i in range(size):
    for j in range(size):
      newMap[i][j] = random.randint(-5, 5)

  return newMap