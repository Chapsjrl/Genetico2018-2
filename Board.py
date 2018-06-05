# -*- coding: utf-8 -*-
"""Clase que contiene el Puzzle a resolver.

Representación de n tablero con N reinas en él. Esta representación esta dada
por un arreglo de n enteros, la posición del numero en el arreglo representa
la columna del tablero y el valor para esa posción representa el renglon que
ocupa la reina en el tablero.

Todas las transformaciones se hacen con intercambios para asegurar que toda la
población sea valida. La representación elegida también evita que existan dos
reinas en la misma coluna o en el mismo renglón, lo que significa que sólo de-
bemos preocuparnos por las reinas en diagonal.

[2, 5, 1, 4, 0, 3]
|_|_|_|_|Q|_|
|_|_|Q|_|_|_|
|Q|_|_|_|_|_|
|_|_|_|_|_|Q|
|_|_|_|Q|_|_|
|_|Q|_|_|_|_|

__author__ = 'Alejandro, Ian, Jess, Ricardo'
__copyright__ = 'Copyright 2018, Chaps'
__license__ = 'MIT'
__version__ = '0.0.1'

"""

import math
import random

# from colorama import Back, Front


class Board:
    """Tablero de ajedrez."""

    def __init__(self, size=6, goal=15):
        """Construye el tablero.

        Args:
            size (int): Tamaño del tablero.
        """
        if size >= 4:
            self.size = size
            self.goal = goal
            self.fitness = 0
            ''' Representamos a las posibles soluciones como una lista de N
            elementos que representa el renglon en que estará colocada la
            reina i.e. [0, 1, 2, 3, 4, 5]'''
            self.queens = list(range(self.size))
            ''' Cambiamos aleatoria mente 3 elementos para obtener un
            arreglo solución valido'''
            self.switch(self.size / 2)
        else:
            print("Tamaño de tablero no valida")

    def switch(self, count):
        """Mueve count reinas de lugar aleatoriamente."""
        for _ in range(int(count)):
            i = random.randint(0, self.size - 1)
            j = random.randint(0, self.size - 1)
            self.queens[i], self.queens[j] = self.queens[j], self.queens[i]

        # Calculamos la aptitud después del movimiento
        self.compute_fitness()

    def regenerate(self):
        """Mueve 3 reinas al azar.

        Usado en la creacion de nuevas generaciones.
        """
        # Movemos dos reinas al azar
        self.switch(2)

        # Mutación con probabilidad de 0.25
        if random.uniform(0, 1) < 0.25:
            self.switch(1)

    def compute_fitness(self):
        """Calcula la aptitud del individuo.

        Un numero más grande es mejor.
        """
        self.fitness = self.goal

        for i in range(self.size):
            for j in range(i + 1, self.size):
                if math.fabs(self.queens[i] - self.queens[j]) == j - i:
                    '''Si las reinas estan en diagonal se reduce la aptitud ya
                    que no pueden encontrarse en la misma columna ni linea'''
                    self.fitness -= 1

    def extract_row(self, queen_pos):
        """Extrae la cadena para cada renglon."""
        queen = self.queens.index(queen_pos)
        row = [('Q' if y == queen else '_') for y in range(self.size)]
        str = '|'.join(row)
        return '|' + str + '|\n'

    def list_coords(self):
        """Extrae la configuracion en un arreglo de tuplas."""
        list = []
        for row in range(self.size):
            queen = self.queens.index(row)
            for col in range(self.size):
                if col == queen:
                    list.append((row, col))
        return list

    def __str__(self):
        """Imprime la configuracion a modo de tablero!."""
        s = list(range(self.size))
        return '\n' + ''.join(list(map(lambda i: self.extract_row(i), s))) \
            + '\n'

    def __rpr__(self):
        """Imprime la configuracion a modo de tablero!."""
        return self.__str__()
