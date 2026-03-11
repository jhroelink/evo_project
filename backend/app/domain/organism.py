from domain.genome import Genome
from domain.environment import Environment
from domain.trait_system import TraitSystem
from domain.map import Map
import random as random

class Organism:
    def __init__(self, genome, x, y):
        self.genome = genome
        self.age = 0
        self.energy = 100
        self.fitness = 0
        self.alive = True
        self.x = x
        self.y = y

    def consume_energy(self, amount):
        self.energy -= amount
        if self.energy <= 0:
            self.energy = 0
            self.alive = False

    def gain_energy(self, amount):
        self.energy += amount
        
    def evaluate_fitness(self, map: Map, trait_system: TraitSystem):
        local_biome = map.get_biome(self.x, self.y)
        self.fitness = trait_system.evaluate(self.genome, local_biome)

    def get_fitness(self, x, y, map: Map, trait_system: TraitSystem):
        local_biome = map.get_biome(x, y)
        return trait_system.evaluate(self.genome, local_biome)
    
    def age_step(self):
        self.age += 1

    def get_neighbouring_fitness(self, x, y, map, trait_system):
        # Make larger moves possible
        dirs = [-1, 0, 1]
        neighbours = []

        for dx in dirs:
            for dy in dirs:

                nx = x + dx
                ny = y + dy

                # Boundary check
                if 0 <= nx < map.width and 0 <= ny < map.height:
                    fitness = self.get_fitness(nx, ny, map, trait_system)
                    neighbours.append((nx, ny, fitness))

        return neighbours


    def move(self, map: Map, trait_system: TraitSystem):
        # Add randomness and traits to move
        neighbours = self.get_neighbouring_fitness(self.x, self.y, map, trait_system)

        best_neighbor = max(neighbours, key=lambda n: n[2])

        self.x = best_neighbor[0]
        self.y = best_neighbor[1]
        self.consume_energy(1)
    
    