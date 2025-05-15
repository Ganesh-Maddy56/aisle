# Problem 2: Game of Life 

# The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead. 
# Every cell interacts with its eight neighbours, 
# which are the cells that are directly horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur: 
    # 1. Any live cell with fewer than two live neighbours dies, as if by loneliness.
    # 2. Any live cell with more than three live neighbours dies, as if by overcrowding. 
    # 3. Any live cell with two or three live neighbours lives, unchanged, to the next generation.
    # 4. Any dead cell with exactly three live neighbours comes to life. 
# The initial pattern constitutes the 'seed' of the system. 
# The first generation is created by applying the above rules simultaneously to every cell in the seed - births and deaths happen simultaneously, and 
# the discrete moment at which this happens is sometimes called a tick. (In other words, each generation is a pure function of the one before.) 
# The rules continue to be applied repeatedly to create further generations. 
# Problem:
    # The below inputs provide the pattern or initial cells in the universe, especially their (x,y) co-ordinates. 
    # The output is the state of the system in the next tick (one run of the application of all the rules) , represented in the same format - i.e. x,y coordinates of all the alive cells after one tick. 


def get_neighbors(cell):
    x, y = cell
    return [
    (x - 1, y - 1),
    (x - 1, y),
    (x - 1, y + 1),
    (x, y - 1),
    (x, y + 1),
    (x + 1, y - 1),
    (x + 1, y),
    (x + 1, y + 1)
]

def next_generation(live_cells):
    neighbor_count = {}
    
    # counting how many times each cell appears as a neighbor
    for cell in live_cells:
        for n in get_neighbors(cell):
            if n in neighbor_count:
                neighbor_count[n] += 1
            else:
                neighbor_count[n] = 1

    new_live_cells = set()
    
    # Game of Life rules:
        # Live cell survives if it has 2 or 3 neighbors
        # Dead cell becomes alive if it has exactly 3 neighbors

    for cell, count in neighbor_count.items():
        if cell in live_cells:
            if count == 2 or count == 3:
                new_live_cells.add(cell)
        else:
            if count == 3:
                new_live_cells.add(cell)
    
    return new_live_cells

def print_cells(cells):
    for x,y in sorted(cells):
        print(f"{x}, {y}")


if __name__ == "__main__":
    # Sample input 1
    inputA = {(1, 1), (1, 2), (2, 1), (2, 2)}
    print("Output A:")
    outputA = next_generation(inputA)
    print_cells(outputA)
    print()

    # Sample input 2
    inputB = {(0, 1), (1, 0), (2, 1), (0, 2), (2, 2)}
    print("Output B:")
    outputB = next_generation(inputB)
    print_cells(outputB)
    print()

    # Sample input 3
    inputC = {(1, 1), (1, 0), (1, 2)}
    print("Output C:")
    outputC = next_generation(inputC)
    print_cells(outputC)
    print()

    # Sample input 4
    inputD = {(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (2, 4)}
    print("Output D:")
    outputD = next_generation(inputD)
    print_cells(outputD)
    print()