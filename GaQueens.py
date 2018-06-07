#!/usr/bin/python3
"""Clase que realiza las operaciones de algoritmos genéticos.

__author__ = 'Alejandro, Ian, Jess, Ricardo'
__copyright__ = 'Copyright 2018, Chaps'
__license__ = 'MIT'
__version__ = '0.0.1'
"""
import copy
import random

from Board import Board


class GaQueens:
    """Algoritmo genético."""

    def __init__(self, board_size, population_size, generation_size):
        """Construye el objeto de algoritmo genético."""
        # Almacena las propiedadeas de la clase
        self.board_size = board_size
        self.population_size = population_size
        self.generation_size = generation_size

        # Cuenta el número de generaciones
        self.generation_count = 0
        # Valor de aptitud para terminar
        self.goal = int((self.board_size * (self.board_size - 1)) / 2)

        # Lista con la poblacion actual
        self.population = []

        # Se crea la primera poblacion
        self.first_generation()
        self.status = ""
        self.solution = Board()

        while True:
            # se detiene si se alcanza la meta
            if self.is_goal_reached() is True:
                break
            # no se crean mas generaciones si se llegó al limite
            if -1 < self.generation_size <= self.generation_count:
                break

            # se crea una nueva generacion a partir de la anterior
            # (Se descarta la generacion anterior)
            self.next_generation()

        # Impresion de resultados
        print("==============================================================\
====")

        # Si no se encuentra la solucion
        if -1 < self.generation_size <= self.generation_count:
            self.status = "No se pudo encontrar solucion en {} generaciones"\
                .format(self.generation_count)
            print(self.status)
        # Si se encuentra la solucion se imprime
        elif self.is_goal_reached():
            self.status = "Se encontro la solucion en la generacion {} "\
                .format(self.generation_count)
            print(self.status)
            for item in self.population:
                if item.fitness == self.goal:
                    # se imprime la lista de la configuracion
                    print(item.queens)
                    # se imprime el objeto con la solucion
                    self.solution = item
                    print(item)

    def is_goal_reached(self):
        """Regresa True si fue alcanzada la meta."""
        for item in self.population:
            if item.fitness == self.goal:
                return True
        return False

    def random_selection(self):
        """Seleciona individuos de esta generacion para la siguiente.

        La seleccion se realiza por medio de la aptitud del individuo y se
        regresa en forma de lista.
        """
        population_list = []
        for i in range(len(self.population)):
            population_list.append((i, self.population[i].fitness))
        population_list.sort(key=lambda pop_item: pop_item[1], reverse=True)
        return population_list[:int(len(population_list) / 3)]

    def first_generation(self):
        """Se crea la primera generación."""
        for i in range(self.population_size):
            self.population.append(Board(self.board_size, self.goal))

        self.print_population()

    def next_generation(self):
        """Crea las siguientes generaciones (excepto la primera)."""
        # agregamos uno al contador de generaciones
        self.generation_count += 1

        # obtenemos la lista de selecionados de esta generacion
        selections = self.random_selection()

        # se crea la nueva generacion a partir de los seleccionados
        new_population = []
        while len(new_population) < self.population_size:
            sel = random.choice(selections)[0]
            new_population.append(copy.deepcopy(self.population[sel]))
        self.population = new_population

        # se realizan cambios aleatorios a la generacion
        for item in self.population:
            item.regenerate()

        self.print_population(selections)

    def print_population(self, selections=None):
        """Imprime la generación actual.

        Generacion #15
            Usando: [1]
            0 : (25) [6, 1, 3, 0, 2, 4, 7, 5]
        linea 1: Generacion #15
            muestra el id de la generación actual
        linea 2: Usando: [1]
            muestra el id de los elementos de la generación anterior
            ocupados para la nueva generación
        linea 3: 0 : (25) [0, 1, 2, 3, 4, 5, 6, 7]
            0 -> id del elemento
            (25) -> aptitud del elemento
            [0, 1, 2, 3, 4, 5, 7] -> posiciones de las reinas en el elemento.
        """
        print("Generacion #%d" % self.generation_count)

        if selections is None:
            selections = []

        print("\tUsando: %s" % str([sel[0] for sel in selections]))

        count = 0
        for item in self.population:
            print("%8d : (%d) %s" %
                  (count, item.fitness, str(item.queens)))
            count += 1
