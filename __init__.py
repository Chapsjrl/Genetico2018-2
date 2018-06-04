import sys

from GaQueens import GaQueens

if __name__ == '__main__':
    # default values
    # size of board also shows how many queens are in game
    board_size = 6
    # size of each generation
    population_size = 10
    # how many generations should I check
    # -1 for no generation limit. (search to find a result)
    generation_size = -1

    # if there is arguments use them instead of default values
    if len(sys.argv) == 4:
        board_size = int(sys.argv[1])
        population_size = int(sys.argv[2])
        generation_size = int(sys.argv[3])

    # print some information about current quest!
    print("Starting:")
    print("    board size      : ", board_size)
    print("    population size : ", population_size)
    print("    generation size : ", generation_size)
    print("==================================================================")

    # Run!
GaQueens(board_size, population_size, generation_size)
