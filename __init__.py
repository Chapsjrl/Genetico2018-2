import sys

from GaQueens import GaQueens

if __name__ == '__main__':
    # Valores por defecto
    # el tamaño por defecto del tablero
    board_size = 8
    # tamaño de cada generación
    population_size = 16
    # número de generaciones que revisará el algoritmo
    # -1 para no tener limite. (Se detendra una vez que encuentra la solución)
    generation_size = 16

    # si se manda a llamar el programa desde linea de comandos con argumentos
    if len(sys.argv) == 4:
        board_size = int(sys.argv[1])
        population_size = int(sys.argv[2])
        generation_size = int(sys.argv[3])

    # Imprime los valores actuales para el algoritmo
    print("Iniciando:")
    print("    Tamano de tablero      : ", board_size)
    print("    Tamano de poblacion    : ", population_size)
    print("    Tamano de generaciones : ", generation_size)
    print("==================================================================")

    # Run!
GaQueens(board_size, population_size, generation_size)
