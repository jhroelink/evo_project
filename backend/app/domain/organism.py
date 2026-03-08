from domain.genome import Genome
from domain.environment import Environment
from domain.trait_system import TraitSystem


class Organism:
    def __init__(self, genome):
        self.genome = genome
        self.age = 0
        self.energy = 100
        self.fitness = 0
        self.alive = True

    def consume_energy(self, amount):
        self.energy -= amount
        if self.energy <= 0:
            self.energy = 0
            self.alive = False

    def gain_energy(self, amount):
        self.energy += amount
        
    def evaluate_fitness(self, environment: Environment, trait_system: TraitSystem):
        self.fitness = trait_system.evaluate(self.genome, environment)

    def age_step(self):
        self.age += 1

    
    