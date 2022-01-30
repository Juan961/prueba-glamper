from utils import findAreas, generate
import os

def clear():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

def main():
  quit = False
  isGenerated = False

  while not quit:
    clear()
    option = int(input("What do you want to do? \n1. Generate a map 1000x1000 \n2. Generate a map nxn \n3. Try with the example image \n4. Quit \n"))
    
    if option == 1:
      newMap = generate()
      isGenerated = True

      while isGenerated:
        option = int(input("What do you want to do? \n1. Find areas (Can generate more of 30000 results!) \n2. Quit \n"))
        if option == 1:
          areas = findAreas(newMap)
          print("Areas: ")
          for i in range(len(areas)):
            print(f"\t{i + 1}. {areas[i]} mt2")

          input("Press enter to continue...")

          isGenerated = False
          break

        elif option == 2:
          isGenerated = False
          break

    elif option == 2:
      size = int(input("Enter the size (square) of the map: "))
      
      newMap = generate(size)

      isGenerated = True
      while isGenerated:
        option = int(input("What do you want to do? \n1. Find areas \n2. Quit \n"))
        if option == 1:
          areas = findAreas(newMap)
          print("Areas: ")
          for i in range(len(areas)):
            print(f"\t{i + 1}. {areas[i]} mt2")

          input("Press enter to continue...")

          isGenerated = False
          break

        elif option == 2:
          isGenerated = False
          break
    
    elif option == 3:
      newMap = [
        [ 2,  1,  3,  5,  8],
        [ 0, -1,  0,  2,  5],
        [ 1, -1, -2,  1,  2],
        [ 1, -2,  2, -1, -2]
      ]

      areas = findAreas(newMap)
      print("Areas: ")
      for i in range(len(areas)):
        print(f"\t{i + 1}. {areas[i]} mt2") 

      input("Press enter to continue...")

    elif option == 4:
      quit = True

    else:
      print("Invalid option")

if __name__ == "__main__":
  main()
