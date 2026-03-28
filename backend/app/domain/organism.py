from domain.genome import Genome
from domain.biome import Biome
from domain.trait_system import TraitSystem
from domain.map import Map
import random as random
import numpy as np
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

    def eat(self, biome, trait_system: TraitSystem):
        efficiency = trait_system.get_trait_value(self.genome, "speed")

        prob = biome.get_food_density() * efficiency

        if random.random() < prob:
            self.gain_energy(np.random.normal(20 * prob, 3))

    def gain_energy(self, amount):
        self.energy += amount
        
    def evaluate_fitness_organism(self, map: Map, trait_system: TraitSystem):
        local_biome = map.get_biome(self.x, self.y)
        self.fitness = trait_system.evaluate_fitness_traits(self.genome, local_biome)

    # def evaluate_energy_organism(self, trait_system: TraitSystem):
    #     energy_cost = trait_system.evaluate_energy_costs_traits(self.genome)
    #     self.consume_energy(energy_cost)

    def get_fitness(self, x, y, map: Map, trait_system: TraitSystem):
        local_biome = map.get_biome(x, y)
        return trait_system.evaluate(self.genome, local_biome)
    
    def reproduction_probability(self):
        return 1 / (1 + np.exp(-self.fitness))  # sigmoid

    def reproduce(self):
        child_genome = self.genome.mutate()

        child = Organism(
            genome=child_genome,
            x=self.x,
            y=self.y
        )

        self.energy -= 30
        return child
    
    def age_step(self):
        self.age += 1

    def can_reproduce(self):
        return self.age > 5 and self.energy > 50
    
    def is_old(self):
        return self.age > 100
    
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


    # Move, more likely to higher fitness areas
    def move(self, map: Map, trait_system: TraitSystem):
        if self.energy < 10:
            return 
        else:
            neighbours = self.get_neighbouring_fitness(self.x, self.y, map, trait_system)

            # Softmax over fitness (temperature controls randomness)
            fitnesses = np.array([n[2] for n in neighbours])
            probs = np.exp(fitnesses) / np.sum(np.exp(fitnesses))

            choice = np.random.choice(len(neighbours), p=probs)
            nx, ny, _ = neighbours[choice]

            self.x = nx
            self.y = ny
            self.consume_energy(1)
        