'''
sudoku_reader.py
Justin Kahr
Reads the sudoku.csv dataset and returns data for neural network use.
'''

# Get n sudoku puzzles as a list of lists
def get_sudoku_n(n):

    if(n > 1000000):
        print("WARNING: Only 10,000 sudokus in dataset.")

    file = open("sudoku.csv", "r")
    dataset = []

    for i in range(n+1):
        line = file.readline().rstrip()
        sudoku = []

        if(i != 0):
            this_puzzle = line.split(",")
            sudoku = [int(d) for d in this_puzzle[0]]
            dataset.append(sudoku)
    return dataset

# Ger n sudoku solutions as a list of lists
def get_solution_n(n):

    if(n > 1000000):
        print("WARNING: Only 10,000 sudokus in dataset.")

    file = open("sudoku.csv", "r")
    dataset = []

    for i in range(n+1):
        line = file.readline().rstrip()
        solution = []

        if(i != 0):
            this_puzzle = line.split(",")
            solution = [int(d) for d in this_puzzle[1]]
            dataset.append(solution)
    return dataset
