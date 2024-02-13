import random

class Popper():
    def __init__(self):
        self.value = "*"
    def unpop(self):
        self.value = chr(random.randint(65, 91))



def print_grid():
    print(f' {grid[0].value} {grid[1].value} {grid[2].value}\n\
{grid[3].value} {grid[4].value} {grid[5].value} {grid[6].value}\n\
 {grid[7].value} {grid[8].value} {grid[9].value}')

def main():
    index = 0
    for spot in grid:
        if random.randint(1,3) <= 2:
            spot.unpop()
            index += 1
            print(index)
    print_grid()
    sInput = input('Quick!\n--------\n: ').upper()
    for popper in grid:
        for char in sInput:
            letters = []
            if not char in letters:
              letters.append(char)
        
        for char in letters:
            if popper.value == char:
                index -= 1
    if index == 0:
      print('lets gooo')

if __name__ == "__main__":
    grid = [Popper() for i in range(10)]
    main()
