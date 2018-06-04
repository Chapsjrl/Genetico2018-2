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
        # store values to class properties
        self.board_size = board_size
        self.population_size = population_size
        self.generation_size = generation_size

        # counts how many generations checked
        self.generation_count = 0
        # fitness value of goal
        self.goal = int((self.board_size * (self.board_size - 1)) / 2)

        # current populations will go here
        self.population = []

        # creates the first population
        self.first_generation()

        while True:
            # if current population reached goal stop checking
            if self.is_goal_reached() is True:
                break
            # don't create more generations if program reached generation_size
            if -1 < self.generation_size <= self.generation_count:
                break

            # create another generation from last generation
            # (discards old generation)
            self.next_generation()

        # prints program result and exits
        print("==============================================================\
        ====")

        # if couldn't find answer
        if -1 < self.generation_size <= self.generation_count:
            print("Couldn't find result in %d generations" %
                  self.generation_count)
        # if there was a result, print it
        elif self.is_goal_reached():
            print("Correct Answer found in generation %s" %
                  self.generation_count)
            for population in self.population:
                if population.fitness == self.goal:
                    # print result as a one lined list
                    print(population.queens)
                    # print result as a nice game board
                    print(population)

    def is_goal_reached(self):
        """Return True if current population reached goal."""
        for population in self.population:
            if population.fitness == self.goal:
                return True
        return False

    def random_selection(self):
        """Select some items from current population for next generation.

        selection are items with highest fit value
        returns a list of selections.
        """
        population_list = []
        for i in range(len(self.population)):
            population_list.append((i, self.population[i].fitness))
        population_list.sort(key=lambda pop_item: pop_item[1], reverse=True)
        return population_list[:int(len(population_list) / 3)]

    def first_generation(self):
        """Create the first generation."""
        for i in range(self.population_size):
            self.population.append(Board(self.board_size, self.goal))

        self.print_population()

    def next_generation(self):
        """Create next generations (all except first one)."""
        # add to generation counter
        self.generation_count += 1

        # get a list of selections to create next generation
        selections = self.random_selection()

        # creates a new population using given selection
        new_population = []
        while len(new_population) < self.population_size:
            sel = random.choice(selections)[0]
            new_population.append(copy.deepcopy(self.population[sel]))
        self.population = new_population

        # make random changes to current population
        for population in self.population:
            population.regenerate()

        self.print_population(selections)

    def print_population(self, selections=None):
        """Print all items in current population.

        Population #15
            Using: [1]
            0 : (25) [6, 1, 3, 0, 2, 4, 7, 5]
        line 1: Population #15
            shows current population id
        line 2: Using: [1]
            shows id of items from last generation
            used for creating current generation
        line 3: 0 : (25) [0, 1, 2, 3, 4, 5, 6, 7]
            0 -> item is
            (25) -> fitness for current item
            [0, 1, 2, 3, 4, 5, 7] -> queen positions in current item.
        """
        print("Population #%d" % self.generation_count)

        if selections is None:
            selections = []

        print("       Using: %s" % str([sel[0] for sel in selections]))

        count = 0
        for population in self.population:
            print("%8d : (%d) %s" %
                  (count, population.fitness, str(population.queens)))
            count += 1
